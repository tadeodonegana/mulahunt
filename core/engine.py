import importlib
import json
from core.config import load_config
from core.db import get_redshift_connection

def run_detection():
    print("[DEBUG] Starting mule detection")
    config = load_config()
    db_conn = get_redshift_connection(config["database"]["redshift"])
    module_scores = {}
    weights = {}

    for mod in config["modules"]:
        if not mod["enabled"]:
            continue
        mod_path, cls_name = mod["class"].rsplit(".", 1)
        mod_cls = getattr(importlib.import_module(mod_path), cls_name)
        instance = mod_cls(db_conn, mod["parameters"])
        scores = instance.run()
        module_scores[mod["name"]] = scores
        weights[mod["name"]] = mod["weight"]

    all_users = set()
    for scores in module_scores.values():
        all_users.update(scores.keys())

    final_results = []
    for user in all_users:
        total_score = 0
        breakdown = {}
        for mod_name, scores in module_scores.items():
            score = scores.get(user, 0)
            # Suma ponderada
            weighted = float(score) * weights[mod_name]
            total_score += weighted
            # Para mostrar mas detalle de por que el modulo lo categorizo con ese scoring
            breakdown[mod_name] = round(score, 2)
        risk_level = "HIGH" if total_score >= 0.7 else "MEDIUM" if total_score >= 0.4 else "LOW"
        print(f"[DEBUG] User {user} => total_score: {total_score}, breakdown: {breakdown}")
        breakdown = {k: float(v) for k, v in breakdown.items()}
        final_results.append((user, round(total_score, 2), risk_level, json.dumps(breakdown)))

    cur = db_conn.cursor()
    for user_id, score, level, breakdown in final_results:
        cur.execute("""
            INSERT INTO user_risk_scores (user_id, risk_score, risk_level, module_scores, last_evaluated)
            VALUES (%s, %s, %s, %s, current_timestamp)
            ON CONFLICT (user_id)
            DO UPDATE SET risk_score=EXCLUDED.risk_score, risk_level=EXCLUDED.risk_level,
                          module_scores=EXCLUDED.module_scores, last_evaluated=current_timestamp;
        """, (user_id, score, level, breakdown))
    print(f"[DEBUG] Final results to insert: {len(final_results)} users")
    db_conn.commit()
    print(f"Updated {len(final_results)} users.")

if __name__ == "__main__":
    run_detection()