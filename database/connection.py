import psycopg2
from database.config import DB_CONFIG


def get_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print("❌ Erro ao conectar ao banco:", e)
        return None
