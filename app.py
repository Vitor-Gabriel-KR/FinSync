from flask import Flask, render_template
from models.saude_financeira_model import get_saude_financeira_mes_atual
from models.previsoes_mes_model import get_previsoes_mes_atual 

app = Flask(__name__)

@app.route("/")
def index():
    dados = get_saude_financeira_mes_atual()
    previsoes = get_previsoes_mes_atual()
    return render_template("index.html", dados=dados, previsoes=previsoes)


if __name__ == "__main__":
    app.run(debug=True)
