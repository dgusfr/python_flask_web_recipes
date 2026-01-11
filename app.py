import json
from flask import Flask, render_template

app = Flask(__name__)


def carregar_dados():
    with open("dados.json", encoding="utf-8") as arquivo:
        return json.load(arquivo)


@app.route("/")
def home():
    todas_receitas = carregar_dados()
    return render_template("index.html", receitas=todas_receitas[:3])


@app.route("/receitas")
def receitas_list():
    todas_receitas = carregar_dados()
    return render_template("recipes.html", receitas=todas_receitas)


@app.route("/receita/<int:id>")
def receita(id):
    todas_receitas = carregar_dados()
    for item in todas_receitas:
        if item["id"] == id:
            return render_template("receita.html", receita=item)
    return "Receita não encontrada!", 404


if __name__ == "__main__":
    app.run(debug=True)
