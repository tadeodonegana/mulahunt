class DetectionModule:
    def __init__(self, db_conn, parameters):
        self.db_conn = db_conn
        self.params = parameters

    def run(self):
        raise NotImplementedError("Each module must implement the run method")