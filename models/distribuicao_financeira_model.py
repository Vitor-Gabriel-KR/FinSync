from database.connection import get_connection
import psycopg2.extras

def get_distribuicao_financeira():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    query = """
        SELECT *
        FROM previsoes_mes
        ORDER BY mes_referencia DESC
        LIMIT 1
    """
    cur.execute(query)
    dados = cur.fetchone()

    cur.close()
    conn.close()
    return dados