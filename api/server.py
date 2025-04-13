from fastapi import FastAPI, HTTPException
from core.config import load_config
from core.db import get_redshift_connection
import json

app = FastAPI()
config = load_config()
db_conn = get_redshift_connection(config["database"]["redshift"])

@app.get("/risk-scores")
def get_all_scores():
    cur = db_conn.cursor()
    cur.execute("SELECT user_id, risk_score, risk_level, last_evaluated FROM user_risk_scores")
    rows = cur.fetchall()
    return {"data": [
        {"user_id": r[0], "risk_score": float(r[1]), "risk_level": r[2], "last_evaluated": r[3].isoformat()} for r in rows
    ]}

@app.get("/risk-scores/{user_id}")
def get_score(user_id: str):
    cur = db_conn.cursor()
    cur.execute("SELECT user_id, risk_score, risk_level, module_scores, last_evaluated FROM user_risk_scores WHERE user_id=%s", (user_id,))
    row = cur.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "user_id": row[0],
        "risk_score": float(row[1]),
        "risk_level": row[2],
        "module_breakdown": json.loads(row[3]),
        "last_evaluated": row[4].isoformat()
    }