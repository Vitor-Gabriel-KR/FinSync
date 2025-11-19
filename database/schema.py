TABLES = {
    "saude_financeira": """
        CREATE TABLE IF NOT EXISTS public.saude_financeira (
            id SERIAL PRIMARY KEY,
            mes_referencia DATE NOT NULL,
            total_receitas NUMERIC(10,2) NOT NULL,
            total_despesas NUMERIC(10,2) NOT NULL,
            lucro_liquido NUMERIC(10,2) NOT NULL,
            investimentos NUMERIC(10,2) NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """,

    "previsoes_mes": """
        CREATE TABLE IF NOT EXISTS public.previsoes_mes (
            id SERIAL PRIMARY KEY,
            mes_referencia DATE,
            salario NUMERIC(10,2),
            custo_vida NUMERIC(10,2),
            gastos_presumidos NUMERIC(10,2),
            investimento NUMERIC(10,2),
            credito NUMERIC(10,2),
            assinaturas NUMERIC(10,2),
            imposto NUMERIC(10,2),
            lucro_liquido NUMERIC(10,2),
            created_at TIMESTAMP
        );
    """,

    "notas_fiscais": """
        CREATE TABLE IF NOT EXISTS public.notas_fiscais (
            id SERIAL PRIMARY KEY,
            numero_nf VARCHAR(50),
            fornecedor VARCHAR(255),
            valor NUMERIC(10,2),
            data_emissao DATE,
            arquivo TEXT,
            timestamp TIMESTAMP,
            mes_referencia VARCHAR(20),
            status VARCHAR(50),
            cliente VARCHAR(255),
            contato VARCHAR(255),
            cnpj VARCHAR(20)
        );
    """,

    "calendario_financeiro": """
    CREATE TABLE IF NOT EXISTS public.calendario_financeiro (
        id SERIAL PRIMARY KEY,
        data_evento DATE,
        categoria VARCHAR(100),
        valor NUMERIC(10,2),
        descricao TEXT,
        timestamp TIMESTAMP,
        pago BOOLEAN,
        ativo BOOLEAN,
        nome VARCHAR(255),
        recorrente BOOLEAN
    );
    """,

    "alertas_lembretes": """
        CREATE TABLE IF NOT EXISTS public.alertas_lembretes (
            id SERIAL PRIMARY KEY,
            titulo TEXT NOT NULL,
            descricao TEXT,
            data_alerta DATE,
            tipo TEXT,
            prioridade TEXT,
            status TEXT DEFAULT 'pendente',
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """
}
