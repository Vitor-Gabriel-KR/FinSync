from database.connection import get_connection
import psycopg2.extras
from datetime import date, datetime
from calendar import monthrange, month_name
import locale

try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
except:
    try:
        locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.UTF-8')
    except:
        pass

class CalendarioService:
    @staticmethod
    def get_calendario_mes(ano=None, mes=None):
        conn = get_connection()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        
        hoje = date.today()
        ano = ano or hoje.year
        mes = mes or hoje.month
        
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
                -- Eventos do mês atual (incluindo inativos)
                (EXTRACT(MONTH FROM data_evento) = %s AND EXTRACT(YEAR FROM data_evento) = %s)
                OR 
                -- Eventos recorrentes ativos
                (recorrente = TRUE AND ativo = TRUE)
            )
            ORDER BY data_evento ASC;
        """
        
        cur.execute(query, (mes, ano))
        dados = cur.fetchall()
        
        eventos_processados = []
        for evento in dados:
            if evento['recorrente'] and evento['ativo']:
                # Para eventos recorrentes ATIVOS, usar o dia do mês original
                dia_original = evento['data_evento'].day
                if dia_original <= ultimo_dia:
                    evento_copia = dict(evento)
                    evento_copia['data_evento'] = date(ano, mes, min(dia_original, ultimo_dia))
                    eventos_processados.append(evento_copia)
            else:
                # Eventos não recorrentes (ativos ou inativos) do mês atual
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
            'primeiro_dia_semana': data_inicio.weekday()
        }

    @staticmethod
    def atualizar_evento(item_id, dados):
        conn = get_connection()
        cur = conn.cursor()

        query = """
            UPDATE calendario_financeiro
            SET nome = %s, valor = %s, pago = %s, recorrente = %s, ativo = %s
            WHERE id = %s;
        """

        cur.execute(query, (
            dados['nome'],
            dados['valor'],
            dados['pago'],
            dados['recorrente'],
            dados['ativo'],
            item_id
        ))
        conn.commit()
        cur.close()
        conn.close()
        return True

    @staticmethod
    def get_evento_por_id(item_id):
        conn = get_connection()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        query = """
            SELECT * FROM calendario_financeiro
            WHERE id = %s;
        """

        cur.execute(query, (item_id,))
        evento = cur.fetchone()
        
        cur.close()
        conn.close()
        return evento

    @staticmethod
    def get_proximo_mes(ano, mes):
        if mes == 12:
            return ano + 1, 1
        return ano, mes + 1

    @staticmethod
    def get_mes_anterior(ano, mes):
        if mes == 1:
            return ano - 1, 12
        return ano, mes - 1