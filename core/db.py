import psycopg2
import os

def get_redshift_connection(config):
    return psycopg2.connect(
        host=config["host"],
        port=config["port"],
        dbname=config["dbname"],
        user=config["user"],
        password=os.getenv("REDSHIFT_PASSWORD")
    )