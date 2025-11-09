from connection import get_connection
from config import TABLES

def test_connection():
    conn = get_connection()
    if not conn:
        return

    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {TABLES['saude_financeira']} ORDER BY id DESC LIMIT 1;")
    row = cursor.fetchone()

    if row:
        print("✅ Conexão bem-sucedida! Último registro:")
        print(row)
    else:
        print("⚠️ Nenhum dado encontrado na tabela.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    test_connection()
