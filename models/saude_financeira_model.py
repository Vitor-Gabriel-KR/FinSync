from database.connection import get_connection
from datetime import date

def get_saude_financeira_mes_atual():
    """Retorna o último registro do mês atual"""
    conn = get_connection()
    cursor = conn.cursor()

    mes_atual = date.today().replace(day=1)

    query = """
        SELECT total_receitas, total_despesas, lucro_liquido, investimentos, timestamp
        FROM saude_financeira
        WHERE mes_referencia = %s
        ORDER BY timestamp DESC
        LIMIT 1
    """

    cursor.execute(query, (mes_atual,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if not result:
        return None

    return {
        "total_receitas": float(result[0]),
        "total_despesas": float(result[1]),
        "lucro_liquido": float(result[2]),
        "investimentos": float(result[3]),
        "timestamp": result[4],
        "mes_atual": mes_atual
    }
