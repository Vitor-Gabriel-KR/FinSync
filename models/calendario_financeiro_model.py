from database.connection import get_connection
import psycopg2.extras
from datetime import date

def get_calendario_mes_atual():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    hoje = date.today()
    mes_atual = hoje.month
    ano_atual = hoje.year

    query = """
        SELECT 
            id,
            nome,
            categoria,
            valor,
            data_evento,
            pago,
            ativo
        FROM calendario_financeiro
        WHERE EXTRACT(MONTH FROM data_evento) = %s
          AND EXTRACT(YEAR FROM data_evento) = %s
          AND (ativo = TRUE OR ativo IS NULL)
        ORDER BY data_evento ASC;
    """

    cur.execute(query, (mes_atual, ano_atual))
    dados = cur.fetchall()

    cur.close()
    conn.close()
    return dados


def atualizar_status_pagamento(item_id, pago):
    conn = get_connection()
    cur = conn.cursor()

    query = """
        UPDATE calendario_financeiro
        SET pago = %s
        WHERE id = %s;
    """

    cur.execute(query, (pago, item_id))
    conn.commit()
    cur.close()
    conn.close()
