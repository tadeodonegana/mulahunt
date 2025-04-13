CREATE TABLE IF NOT EXISTS transactions (
    transaction_id SERIAL PRIMARY KEY,
    user_id        INTEGER,
    amount         NUMERIC(12,2),
    timestamp      TIMESTAMP,
    description    TEXT
);

CREATE TABLE IF NOT EXISTS user_risk_scores (
    user_id        INTEGER PRIMARY KEY,
    risk_score     FLOAT,
    risk_level     VARCHAR(10),
    module_scores  TEXT,
    last_evaluated TIMESTAMP
);
