from modules.base import DetectionModule
class TxFrequencyModule(DetectionModule):
    def run(self):
        cur = self.db_conn.cursor()
        query = f"""
            SELECT user_id, COUNT(*) as tx_count
            FROM transactions
            WHERE timestamp >= CURRENT_DATE - interval '{self.params['window_days']} day'
            GROUP BY user_id;
        """
        cur.execute(query)
        rows = cur.fetchall()
        result = {}
        for user_id, count in rows:
            score = min(count / self.params['tx_count_threshold'], 1.0)
            result[user_id] = score
        return result