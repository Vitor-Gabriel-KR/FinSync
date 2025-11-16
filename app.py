from flask import Flask, render_template, jsonify, request
from models.saude_financeira_model import get_saude_financeira_mes_atual
from models.previsoes_mes_model import get_previsoes_mes_atual
from models.distribuicao_financeira_model import get_distribuicao_financeira
from models.notas_fiscais_model import get_notas_fiscais, update_status_nota
from models.calendario_financeiro_model import CalendarioService
from datetime import date

app = Flask(__name__)

@app.template_filter('format_currency')
def format_currency(value):
    if value is None:
        return "0,00"
    return "{:,.2f}".format(float(value)).replace(",", "X").replace(".", ",").replace("X", ".")

@app.route("/")
def index():
    dados = get_saude_financeira_mes_atual()
    previsoes = get_previsoes_mes_atual()
    distribuicao = get_distribuicao_financeira()
    notas = get_notas_fiscais()
    
    ano = request.args.get('ano', type=int)
    mes = request.args.get('mes', type=int)
    
    dados_calendario = CalendarioService.get_calendario_mes(ano, mes)
    
    hoje = date.today()
    mes_anterior = CalendarioService.get_mes_anterior(
        dados_calendario['ano'], 
        dados_calendario['mes']
    )
    proximo_mes = CalendarioService.get_proximo_mes(
        dados_calendario['ano'], 
        dados_calendario['mes']
    )

    return render_template(
        "index.html",
        dados=dados,
        previsoes=previsoes,
        distribuicao=distribuicao,
        notas=notas,
        hoje=hoje,
        mes_anterior=mes_anterior,
        proximo_mes=proximo_mes,
        **dados_calendario
    )

@app.route("/atualizar_status", methods=["POST"])
def atualizar_status():
    data = request.get_json()
    numero_nf = data.get("numero_nf")
    novo_status = data.get("status")

    if not numero_nf or not novo_status:
        return jsonify({"success": False, "error": "Dados inválidos"}), 400

    try:
        update_status_nota(numero_nf, novo_status)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/atualizar_evento", methods=["POST"])
def atualizar_evento():
    data = request.get_json()
    item_id = data.get("id")
    
    if not item_id:
        return jsonify({"success": False, "error": "ID do evento é obrigatório"}), 400

    try:
        dados_atualizacao = {
            'nome': data.get('nome'),
            'valor': float(data.get('valor', 0)),
            'pago': data.get('pago', False),
            'recorrente': data.get('recorrente', False),
            'ativo': data.get('ativo', True)
        }
        
        CalendarioService.atualizar_evento(item_id, dados_atualizacao)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/get_evento/<int:evento_id>")
def get_evento(evento_id):
    try:
        evento = CalendarioService.get_evento_por_id(evento_id)
        if evento:
            return jsonify({
                'success': True,
                'evento': {
                    'id': evento['id'],
                    'nome': evento['nome'],
                    'valor': float(evento['valor']),
                    'pago': evento['pago'],
                    'recorrente': evento['recorrente'],
                    'ativo': evento['ativo'],
                    'categoria': evento['categoria']
                }
            })
        else:
            return jsonify({'success': False, 'error': 'Evento não encontrado'}), 404
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)