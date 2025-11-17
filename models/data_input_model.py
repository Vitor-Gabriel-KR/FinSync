from database.connection import get_connection
import psycopg2.extras

def insert_calendario_financeiro(data_evento, categoria, valor, descricao, nome, pago=False, recorrente=False):
    conn = get_connection()
    cur = conn.cursor()
    
    query = """
        INSERT INTO calendario_financeiro 
        (data_evento, categoria, valor, descricao, nome, pago, recorrente)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    
    cur.execute(query, (data_evento, categoria, valor, descricao, nome, pago, recorrente))
    conn.commit()
    
    cur.close()
    conn.close()
    return True

def insert_nota_fiscal(numero_nf, fornecedor, valor, data_emissao, mes_referencia, status, cliente, contato, cnpj):
    conn = get_connection()
    cur = conn.cursor()
    
    query = """
        INSERT INTO notas_fiscais 
        (numero_nf, fornecedor, valor, data_emissao, mes_referencia, status, cliente, contato, cnpj)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    cur.execute(query, (numero_nf, fornecedor, valor, data_emissao, mes_referencia, status, cliente, contato, cnpj))
    conn.commit()
    
    cur.close()
    conn.close()
    return True

def insert_previsao_mes(mes_referencia, salario, custo_vida, gastos_presumidos, investimento, credito, assinaturas, imposto):
    conn = get_connection()
    cur = conn.cursor()
    
    query = """
        INSERT INTO previsoes_mes 
        (mes_referencia, salario, custo_vida, gastos_presumidos, investimento, credito, assinaturas, imposto)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    cur.execute(query, (mes_referencia, salario, custo_vida, gastos_presumidos, investimento, credito, assinaturas, imposto))
    conn.commit()
    
    cur.close()
    conn.close()
    return True