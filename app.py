from flask import Flask, render_template, jsonify, request
from models.saude_financeira_model import get_saude_financeira_mes_atual
from models.previsoes_mes_model import get_previsoes_mes_atual
from models.notas_fiscais_model import get_notas_fiscais, update_status_nota

app = Flask(__name__)

@app.route("/")
def index():
    dados = get_saude_financeira_mes_atual()
    previsoes = get_previsoes_mes_atual()
    notas = get_notas_fiscais()
    return render_template("index.html", dados=dados, previsoes=previsoes, notas=notas)

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


if __name__ == "__main__":
    app.run(debug=True)
