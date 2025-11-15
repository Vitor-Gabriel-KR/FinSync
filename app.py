from flask import Flask, render_template, jsonify, request
from models.saude_financeira_model import get_saude_financeira_mes_atual
from models.previsoes_mes_model import get_previsoes_mes_atual
from models.notas_fiscais_model import get_notas_fiscais, update_status_nota
from models.calendario_financeiro_model import CalendarioService
from datetime import date

app = Flask(__name__)

@app.route("/")
def index():
    dados = get_saude_financeira_mes_atual()
    previsoes = get_previsoes_mes_atual()
    notas = get_notas_fiscais()
    
    # Obter parâmetros de ano e mês para o calendário
    ano = request.args.get('ano', type=int)
    mes = request.args.get('mes', type=int)
    
    # Dados do calendário
    dados_calendario = CalendarioService.get_calendario_mes(ano, mes)
    
    # Calcular mês anterior e próximo
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

@app.route("/atualizar_pagamento", methods=["POST"])
def atualizar_pagamento():
    data = request.get_json()
    item_id = data.get("item_id")
    pago = data.get("pago")

    if item_id is None or pago is None:
        return jsonify({"success": False, "error": "Dados inválidos"}), 400

    try:
        CalendarioService.atualizar_status_pagamento(item_id, pago)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)