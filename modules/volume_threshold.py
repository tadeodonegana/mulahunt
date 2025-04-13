from modules.base import DetectionModule
class VolumeThresholdModule(DetectionModule):
    def run(self):
        cur = self.db_conn.cursor()
        query = f"""
            SELECT user_id, SUM(amount) as total_volume
            FROM transactions
            WHERE timestamp >= CURRENT_DATE - interval '{self.params['window_days']} day'
            GROUP BY user_id;
        """
        cur.execute(query)
        rows = cur.fetchall()
        result = {}
        for user_id, volume in rows:
            score = min(volume / self.params['volume_threshold'], 1.0)
            result[user_id] = score
        return result