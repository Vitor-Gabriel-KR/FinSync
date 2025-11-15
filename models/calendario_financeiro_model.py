from database.connection import get_connection
import psycopg2.extras
from datetime import date, datetime
from calendar import monthrange, month_name
import locale

# Configurar locale para português
try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
except:
    try:
        locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.UTF-8')
    except:
        pass  # Usar locale padrão se não conseguir configurar

class CalendarioService:
    @staticmethod
    def get_calendario_mes(ano=None, mes=None):
        """Busca eventos do mês especificado, incluindo recorrentes"""
        conn = get_connection()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        
        hoje = date.today()
        ano = ano or hoje.year
        mes = mes or hoje.month
        
        # Calcular primeiro e último dia do mês
        _, ultimo_dia = monthrange(ano, mes)
        data_inicio = date(ano, mes, 1)
        
        query = """
            SELECT 
                id,
                nome,
                categoria,
                valor,
                data_evento,
                pago,
                ativo,
                recorrente
            FROM calendario_financeiro
            WHERE (
                -- Eventos do mês atual
                (EXTRACT(MONTH FROM data_evento) = %s AND EXTRACT(YEAR FROM data_evento) = %s)
                OR 
                -- Eventos recorrentes (qualquer data, mas aparecem todo mês)
                (recorrente = TRUE AND ativo = TRUE)
            )
            AND (ativo = TRUE OR ativo IS NULL)
            ORDER BY data_evento ASC;
        """
        
        cur.execute(query, (mes, ano))
        dados = cur.fetchall()
        
        # Processar eventos recorrentes
        eventos_processados = []
        for evento in dados:
            if evento['recorrente']:
                # Para eventos recorrentes, usar o dia do mês original
                dia_original = evento['data_evento'].day
                if dia_original <= ultimo_dia:
                    evento_copia = dict(evento)
                    evento_copia['data_evento'] = date(ano, mes, min(dia_original, ultimo_dia))
                    eventos_processados.append(evento_copia)
            else:
                # Verificar se o evento não recorrente pertence ao mês atual
                if evento['data_evento'].month == mes and evento['data_evento'].year == ano:
                    eventos_processados.append(evento)
        
        cur.close()
        conn.close()
        
        return {
            'eventos': eventos_processados,
            'ano': ano,
            'mes': mes,
            'mes_nome': month_name[mes].capitalize(),
            'dias_no_mes': ultimo_dia,
            'primeiro_dia_semana': data_inicio.weekday()  # 0=Segunda, 6=Domingo
        }

    @staticmethod
    def atualizar_status_pagamento(item_id, pago):
        """Atualiza status de pagamento"""
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
        return True

    @staticmethod
    def get_proximo_mes(ano, mes):
        """Calcula próximo mês para navegação"""
        if mes == 12:
            return ano + 1, 1
        return ano, mes + 1

    @staticmethod
    def get_mes_anterior(ano, mes):
        """Calcula mês anterior para navegação"""
        if mes == 1:
            return ano - 1, 12
        return ano, mes - 1