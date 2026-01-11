import json
from flask import Flask, render_template, request

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
    termo = request.args.get("q")

    if termo:
        receitas_filtradas = []
        for receita in todas_receitas:
            nome_receita = receita["titulo"].lower()
            termo_pesquisa = termo.lower()
            if termo_pesquisa in nome_receita:
                receitas_filtradas.append(receita)
        return render_template("recipes.html", receitas=receitas_filtradas)

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
