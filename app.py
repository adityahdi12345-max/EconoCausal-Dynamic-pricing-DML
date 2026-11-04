import streamlit as st
import pandas as pd, numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from dml_engine import estimate_plr_dml

st.set_page_config(page_title="EconoCausal", page_icon="📈", layout="wide")
st.markdown("""<style>
.block-container{padding-top:1.3rem}
.hero{padding:1.3rem;border-radius:15px;background:linear-gradient(110deg,#10234b,#28558c);color:white}
.hero h1{color:white;margin:0}.hero p{color:#dce8ff;margin:5px 0 0}
div[data-testid="stMetric"]{background:#f4f7fc;border:1px solid #e1e8f2;padding:12px;border-radius:12px}
</style><div class="hero"><h1>ECONOCAUSAL</h1><p>Dynamic Pricing Analytics • Double Machine Learning • Decision Support</p></div>""", unsafe_allow_html=True)

up=st.sidebar.file_uploader("Upload Online Retail.xlsx / CSV",type=["xlsx","xls","csv"])
if up is None:
    st.info("Upload your Online Retail dataset from the left sidebar to open the live dashboard.")
    st.markdown("### Dashboard modules")
    a,b,c,d=st.columns(4)
    for col,title,desc in zip([a,b,c,d],["Executive Summary","EDA & Insights","DML Estimation","Future Roadmap"],
      ["Dataset KPIs and quality","Sales, price and demand patterns","Cross-fitted DML prototype","Validation and deployment plan"]):
        col.subheader(title); col.caption(desc)
    st.stop()

df=pd.read_excel(up) if up.name.lower().endswith((".xlsx",".xls")) else pd.read_csv(up)
df.columns=[str(c).strip() for c in df.columns]
def find(names):
    lookup={c.lower().replace(" ","").replace("_",""):c for c in df.columns}
    for n in names:
        k=n.lower().replace(" ","").replace("_","")
        if k in lookup:return lookup[k]
    return None
q=find(["Quantity","Qty"]); p=find(["UnitPrice","Unit Price","Price"])
dt=find(["InvoiceDate","Date"]); product=find(["Description","Product"]); country=find(["Country"])
if q and p:
    df[q]=pd.to_numeric(df[q],errors="coerce"); df[p]=pd.to_numeric(df[p],errors="coerce")
    df["TotalSales"]=df[q]*df[p]

tabs=st.tabs(["Executive Summary","EDA & Insights","DML & Uplift","Causal Design","Future Work"])
with tabs[0]:
    st.subheader("Executive Summary")
    a,b,c,d=st.columns(4)
    a.metric("Records",f"{len(df):,}"); b.metric("Columns",len(df.columns))
    c.metric("Missing cells",f"{int(df.isna().sum().sum()):,}")
    d.metric("Observed sales",f"{df['TotalSales'].sum():,.2f}" if "TotalSales" in df else "N/A")
    st.dataframe(df.head(15),use_container_width=True)
    quality=pd.DataFrame({"Missing":df.isna().sum(),"Missing %":(df.isna().mean()*100).round(2),"Unique":df.nunique()})
    st.subheader("Data quality profile"); st.dataframe(quality,use_container_width=True)
with tabs[1]:
    st.subheader("Exploratory Data Analysis")
    if q and p:
        v=df.dropna(subset=[q,p]).copy(); v=v[(v[q]>0)&(v[p]>0)]; v["TotalSales"]=v[q]*v[p]
        a,b,c=st.columns(3); a.metric("Valid rows",f"{len(v):,}"); b.metric("Mean price",f"{v[p].mean():.2f}"); c.metric("Mean quantity",f"{v[q].mean():.2f}")
        for col,title in [(p,"Unit price distribution"),(q,"Quantity distribution")]:
            fig,ax=plt.subplots(); sns.histplot(v[col],bins=40,kde=True,ax=ax); ax.set_title(title); st.pyplot(fig); plt.close(fig)
        fig,ax=plt.subplots(); sample=v[[p,q]].sample(min(4000,len(v)),random_state=42)
        sns.scatterplot(data=sample,x=p,y=q,alpha=.3,ax=ax); ax.set_title("Observed price vs quantity")
        st.pyplot(fig); plt.close(fig)
        fig,ax=plt.subplots(); sns.boxplot(x=v["TotalSales"],ax=ax); ax.set_title("Transaction sales outliers")
        st.pyplot(fig); plt.close(fig)
        if product:
            top=v.groupby(product)["TotalSales"].sum().nlargest(10).reset_index()
            st.subheader("Top 10 products by observed revenue"); st.dataframe(top,use_container_width=True)
            fig,ax=plt.subplots(figsize=(9,5)); sns.barplot(data=top,x="TotalSales",y=product,ax=ax)
            st.pyplot(fig); plt.close(fig)
        if dt:
            v[dt]=pd.to_datetime(v[dt],errors="coerce")
            monthly=v.dropna(subset=[dt]).set_index(dt).resample("MS")["TotalSales"].sum().reset_index()
            fig,ax=plt.subplots(figsize=(10,4)); sns.lineplot(data=monthly,x=dt,y="TotalSales",marker="o",ax=ax)
            ax.set_title("Monthly observed revenue"); st.pyplot(fig); plt.close(fig)
    else: st.warning("Could not detect Quantity and UnitPrice columns.")
    num=df.select_dtypes(include=np.number)
    if len(num.columns)>1:
        st.subheader("Correlation heatmap (descriptive, not causal)")
        fig,ax=plt.subplots(figsize=(9,6)); sns.heatmap(num.corr(),cmap="vlag",center=0,ax=ax)
        st.pyplot(fig); plt.close(fig)
with tabs[2]:
    st.subheader("Double Machine Learning — exploratory estimation")
    st.warning("Do not treat this estimate as causal unless the confounders and identification assumptions are defensible.")
    numeric=df.select_dtypes(include=np.number).columns.tolist()
    if q in numeric and p in numeric:
        y=st.selectbox("Outcome (Y)",numeric,index=numeric.index(q))
        t=st.selectbox("Treatment (T)",numeric,index=numeric.index(p))
        candidates=[x for x in df.columns if x not in [y,t]]
        defaults=[x for x in [product,country] if x in candidates]
        xs=st.multiselect("Potential pre-treatment confounders (X)",candidates,default=defaults)
        folds=st.selectbox("Cross-fitting folds",[3,5,10],index=1)
        if st.button("Estimate exploratory DML effect",type="primary"):
            try:
                result=estimate_plr_dml(df,t,y,xs,folds)
                a,b,c=st.columns(3); a.metric("Estimated effect",f"{result['estimate']:.5f}")
                b.metric("Standard error",f"{result['std_error']:.5f}")
                c.metric("95% confidence interval",f"[{result['ci_low']:.5f}, {result['ci_high']:.5f}]")
                st.json(result); st.warning(result["warning"])
            except Exception as e: st.error(str(e))
    else: st.info("Numeric Quantity and UnitPrice columns are required for the suggested DML setup.")
with tabs[3]:
    st.subheader("Causal design")
    st.markdown("""
    - **Treatment (T):** Unit price
    - **Outcome (Y):** Quantity purchased
    - **Confounders (X):** Defensible pre-treatment factors that influence both price and demand

    **Assumptions to assess:** no important unmeasured confounding, sufficient overlap, consistent treatment/outcome definitions, and no post-treatment controls.

    **DML workflow:** cross-fit outcome and treatment models → calculate residuals → estimate the effect from residualized treatment and outcome.
    """)
    st.code("Y = theta * T + g(X) + error\\nT = m(X) + v")
with tabs[4]:
    st.subheader("Future Work Roadmap")
    roadmap=pd.DataFrame([
    ["Richer data","Competitor prices, promotions, costs","Planned"],
    ["Causal validation","Confounder review and sensitivity","Planned"],
    ["Advanced methods","Compare DML specifications","Planned"],
    ["Experimentation","Controlled A/B tests where feasible","Planned"],
    ["Deployment","API and interactive dashboard","In progress"],
    ["Scalability","More products and regions","Planned"]],
    columns=["Workstream","Activity","Status"])
    st.dataframe(roadmap,use_container_width=True)
    st.caption("Roadmap items are planned, not completed capabilities.")
st.divider()
st.caption("EconoCausal | Aditya Mishra | Mid-review dashboard prototype")
