from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import pandas as pd
from dml_engine import estimate_plr_dml

app=FastAPI(title="EconoCausal API",version="1.0")
class Request(BaseModel):
    records: List[dict]
    treatment: str
    outcome: str
    confounders: List[str]
    n_splits: int=5

@app.get("/")
def home():
    return {"project":"EconoCausal","status":"API running"}

@app.post("/dml-estimate")
def dml(req:Request):
    try:
        return estimate_plr_dml(pd.DataFrame(req.records),req.treatment,req.outcome,req.confounders,req.n_splits)
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))
