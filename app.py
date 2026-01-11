import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    with open("dados.json", encoding="utf-8") as arquivo:
        lista_receitas = json.load(arquivo)

    return render_template("index.html", receitas=lista_receitas)


@app.route("/receita/<int:id>")
def receita(id):
    with open("dados.json", encoding="utf-8") as arquivo:
        lista_receitas = json.load(arquivo)

    receita_encontrada = None
    for item in lista_receitas:
        if item["id"] == id:
            receita_encontrada = item
            break

    if receita_encontrada:
        return render_template("receita.html", receita=receita_encontrada)
    else:
        return "Receita não encontrada!", 404


@app.route("/sobre")
def about():
    with open("dados.json", encoding="utf-8") as arquivo:
        lista_receitas = json.load(arquivo)
    return render_template("about.html", receitas=lista_receitas[:3])


@app.route("/contato")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
