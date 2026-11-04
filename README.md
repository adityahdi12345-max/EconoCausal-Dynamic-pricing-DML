# EconoCausal Interactive Dashboard
**Author:** Aditya Mishra

## Run the dashboard
1. Extract this ZIP.
2. Open a terminal in the extracted folder.
3. Install packages: `pip install -r requirements.txt`
4. Start frontend/dashboard: `streamlit run app.py`
5. Upload `Online Retail.xlsx` in the left sidebar.

## Optional FastAPI backend
In another terminal run: `uvicorn api:app --reload`
Open `http://127.0.0.1:8000/docs` for API documentation.

## Important
The DML implementation is an exploratory cross-fitted partially-linear DML prototype using Random Forest nuisance models. A numerical estimate is not automatically causal. Carefully justify treatment, outcome, pre-treatment confounders, overlap, no-unmeasured-confounding, consistency, and robustness before presenting a causal claim. Do not use post-treatment or outcome-derived variables as controls.
