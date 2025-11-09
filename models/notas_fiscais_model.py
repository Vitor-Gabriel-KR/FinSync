from database.connection import get_connection
import psycopg2.extras

def get_notas_fiscais():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    query = """
        SELECT 
            id,
            numero_nf,
            fornecedor,
            valor,
            data_emissao,
            arquivo,
            timestamp,
            mes_referencia,
            status,
            cliente
        FROM notas_fiscais
        ORDER BY data_emissao DESC;
    """

    cur.execute(query)
    dados = cur.fetchall()

    cur.close()
    conn.close()
    return dados

def update_status_nota(numero_nf, novo_status):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE notas_fiscais
        SET status = %s
        WHERE numero_nf = %s
    """, (novo_status, numero_nf))
    conn.commit()
    cur.close()
    conn.close()