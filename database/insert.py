from connection import get_connection
from datetime import date

def insert_sample():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO saude_financeira (total_receitas, total_despesas, impostos, mes_referencia)
        VALUES (%s, %s, %s, %s)
    """
    dados = (3000, 2300, 80, date.today().replace(day=1))

    cursor.execute(query, dados)
    conn.commit()

    print("✅ Registro inserido com sucesso!")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    insert_sample()
