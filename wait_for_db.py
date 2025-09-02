import os
import time
import psycopg2
from psycopg2 import OperationalError

def wait_for_db():
    db_name = os.getenv("POSTGRES_DB")
    db_user = os.getenv("POSTGRES_USER")
    db_password = os.getenv("POSTGRES_PASSWORD")
    db_host = os.getenv("DB_HOST", "db")
    db_port = os.getenv("DB_PORT","5432")

    while True:
        try:
            connection = psycopg2.connect(
                dbname = db_name,
                user = db_user,
                password = db_password,
                host = db_host,
                port = db_port
            )
            connection.close()
            print("Database is ready!")
            break
        except OperationalError:
            print("Database not ready, waiting for 1 second")
            time.sleep(1)

if __name__ == "__main__":
    wait_for_db()