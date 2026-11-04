import numpy as np, pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold
from sklearn.base import clone

def _preprocessor(X):
    num=X.select_dtypes(include=["number"]).columns.tolist()
    cat=[c for c in X.columns if c not in num]
    transformers=[]
    if num:
        transformers.append(("num",Pipeline([("imp",SimpleImputer(strategy="median")),("scale",StandardScaler())]),num))
    if cat:
        transformers.append(("cat",Pipeline([("imp",SimpleImputer(strategy="most_frequent")),("oh",OneHotEncoder(handle_unknown="ignore"))]),cat))
    return ColumnTransformer(transformers)

def estimate_plr_dml(data,treatment,outcome,confounders,n_splits=5,random_state=42):
    if not confounders: raise ValueError("Select at least one defensible pre-treatment confounder.")
    work=data[[treatment,outcome]+list(confounders)].copy()
    work[treatment]=pd.to_numeric(work[treatment],errors="coerce")
    work[outcome]=pd.to_numeric(work[outcome],errors="coerce")
    work=work.replace([np.inf,-np.inf],np.nan).dropna(subset=[treatment,outcome])
    if len(work)<max(100,n_splits*10): raise ValueError(f"Not enough usable rows: {len(work)}")
    if work[treatment].nunique()<5: raise ValueError("Treatment has too few distinct values.")
    X=work[list(confounders)]; y=work[outcome].to_numpy(float); t=work[treatment].to_numpy(float)
    xp=_preprocessor(X).fit_transform(X)
    if hasattr(xp,"toarray"): xp=xp.toarray()
    my=RandomForestRegressor(n_estimators=120,min_samples_leaf=10,random_state=random_state,n_jobs=-1)
    mt=RandomForestRegressor(n_estimators=120,min_samples_leaf=10,random_state=random_state+1,n_jobs=-1)
    yh=np.zeros(len(work)); th=np.zeros(len(work))
    for tr,te in KFold(n_splits=n_splits,shuffle=True,random_state=random_state).split(xp):
        yh[te]=clone(my).fit(xp[tr],y[tr]).predict(xp[te])
        th[te]=clone(mt).fit(xp[tr],t[tr]).predict(xp[te])
    yr=y-yh; tr=t-th; den=np.sum(tr**2)
    if den<1e-10: raise ValueError("Residualized treatment has almost no variation.")
    theta=float(np.sum(tr*yr)/den); eps=yr-theta*tr
    se=float(np.sqrt(np.mean((tr*eps)**2))/max(np.mean(tr**2),1e-12)/np.sqrt(len(work)))
    return {"estimate":theta,"std_error":se,"ci_low":theta-1.96*se,"ci_high":theta+1.96*se,
      "rows_used":len(work),"treatment":treatment,"outcome":outcome,"confounders":list(confounders),
      "warning":"Exploratory observational DML estimate. Causal interpretation requires valid pre-treatment confounders, no important unmeasured confounding, overlap, consistency, and robustness checks."}
