import psycopg2
from psycopg2 import sql, OperationalError

import os
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host = os.getenv("HOST"),
            user = os.getenv("USER"),
            password = os.getenv("PASSWORD"),
            database = os.getenv("DATABASE"),
            port = os.getenv("PORT")
        )
        print("Database connected successfully")
        return conn
    except OperationalError as e:
        print(f"{e}")
        return None

conn = get_db_connection()