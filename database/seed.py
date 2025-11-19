SEEDS = {
    "saude_financeira": [
        """
        INSERT INTO public.saude_financeira 
            (mes_referencia, total_receitas, total_despesas, lucro_liquido, investimentos, timestamp)
        VALUES
            ('2025-11-01', 3000.00, 2331.00, 669.00, 500.00, '2025-11-09 15:22:51.742475');
        """
    ],

    "previsoes_mes": [
        """
        INSERT INTO public.previsoes_mes
            (mes_referencia, salario, custo_vida, gastos_presumidos, investimento, credito, assinaturas, imposto, lucro_liquido, created_at)
        VALUES
            ('2025-11-01', 3000.00, 600.00, 560.00, 500.00, 377.00, 214.00, 80.00, 669.00, '2025-11-09 15:47:21.912701');

        """
    ],

    "notas_fiscais": [
        """
        INSERT INTO public.notas_fiscais
        (numero_nf, fornecedor, valor, data_emissao, arquivo, timestamp, mes_referencia, status, cliente, contato, cnpj)
        VALUES ('00125', 'Mextech Tecnologia Industrial', 3000, '2025-11-05', 'file:///C:/Users/Nome%20Colaborador/Downloads/NF%2030102025.pdf', '2025-11-09 17:25:10.736556', '11/2025', 'Pendente', 'Mextech', 'paulino.mexiajr@mextech.com.br', '12.345.678/0001-90');
        """,
        """
        INSERT INTO public.notas_fiscais
        (numero_nf, fornecedor, valor, data_emissao, arquivo, timestamp, mes_referencia, status, cliente, contato, cnpj)
        VALUES ('00127', 'Cliente C', 457, '2025-10-28', 'file:///C:/Users/Nome%20Colaborador/Downloads/NF%2030102025.pdf', '2025-11-09 17:25:10.736556', '10/2025', 'Emitida', 'Cliente C', 'dev@clientec.com', '45.876.123/0001-33');
        """,
        """
        INSERT INTO public.notas_fiscais
        (numero_nf, fornecedor, valor, data_emissao, arquivo, timestamp, mes_referencia, status, cliente, contato, cnpj)
        VALUES ('00126', 'Cliente B', 200, '2025-11-03', 'file:///C:/Users/Nome%20Colaborador/Downloads/NF%2030102025.pdf', '2025-11-09 17:25:10.736556', '11/2025', 'Atrasada', 'Cliente B', 'suporte@clienteb.com', '98.765.432/0001-09');
        """,
        """
        INSERT INTO public.notas_fiscais
        (numero_nf, fornecedor, valor, data_emissao, arquivo, timestamp, mes_referencia, status, cliente, contato, cnpj)
        VALUES ('00128', 'Cliente D', 12, '2025-11-04', NULL, '2025-11-17 09:30:40.305919', '2025-11', 'pago', 'Cliente D', '', '');
        """
    ],

    "calendario_financeiro": [
        """
        INSERT INTO public.calendario_financeiro
        (data_evento, categoria, valor, descricao, timestamp, pago, ativo, nome, recorrente)
        VALUES ('2025-11-05', 'salário', 3000, NULL, '2025-11-09 18:56:57.007516', TRUE, TRUE, 'salário mensal', TRUE);
        """,

        """
        INSERT INTO public.calendario_financeiro
        (data_evento, categoria, valor, descricao, timestamp, pago, ativo, nome, recorrente)
        VALUES ('2025-11-05', 'crédito', 0, NULL, '2025-11-09 18:56:57.007516', FALSE, TRUE, 'cartão pj', TRUE);
        """,

        """
        INSERT INTO public.calendario_financeiro
        (data_evento, categoria, valor, descricao, timestamp, pago, ativo, nome, recorrente)
        VALUES ('2025-11-20', 'imposto', 80, NULL, '2025-11-09 18:56:57.007516', TRUE, TRUE, 'das mei', TRUE);
        """,

        """
        INSERT INTO public.calendario_financeiro
        (data_evento, categoria, valor, descricao, timestamp, pago, ativo, nome, recorrente)
        VALUES ('2025-11-24', 'crédito', 457, NULL, '2025-11-09 18:56:57.007516', FALSE, TRUE, 'cartão pessoal', TRUE);
        """,

        """
        INSERT INTO public.calendario_financeiro
        (data_evento, categoria, valor, descricao, timestamp, pago, ativo, nome, recorrente)
        VALUES ('2025-11-26', 'assinatura', 12.99, NULL, '2025-11-09 18:56:57.007516', TRUE, TRUE, 'clube ifood', TRUE);
        """,

        """
        INSERT INTO public.calendario_financeiro
        (data_evento, categoria, valor, descricao, timestamp, pago, ativo, nome, recorrente)
        VALUES ('2025-11-05', 'assinatura', 35.99, NULL, '2025-11-09 18:56:57.007516', TRUE, FALSE, 'Aplicativo', FALSE);
        """,

        """
        INSERT INTO public.calendario_financeiro
        (data_evento, categoria, valor, descricao, timestamp, pago, ativo, nome, recorrente)
        VALUES ('2025-11-10', 'assinatura', 149.90, NULL, '2025-11-09 18:56:57.007516', TRUE, TRUE, 'smartfit', TRUE);
        """,

        """
        INSERT INTO public.calendario_financeiro
        (data_evento, categoria, valor, descricao, timestamp, pago, ativo, nome, recorrente)
        VALUES ('2025-11-06', 'assinatura', 15, NULL, '2025-11-09 18:56:57.007516', TRUE, TRUE, 'crunchyroll', TRUE);
        """,

        """
        INSERT INTO public.calendario_financeiro
        (data_evento, categoria, valor, descricao, timestamp, pago, ativo, nome, recorrente)
        VALUES ('2025-11-15', 'assinatura', 70, NULL, '2025-11-09 18:56:57.007516', TRUE, TRUE, 'gamepass', FALSE);
        """
    ],

    "alertas_lembretes": [
        """
        INSERT INTO public.alertas_lembretes (titulo)
        VALUES ('');
        """
    ]
}
