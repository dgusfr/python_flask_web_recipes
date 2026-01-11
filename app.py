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
    # 1. Carrega os dados (igual na home)
    with open("dados.json", encoding="utf-8") as arquivo:
        lista_receitas = json.load(arquivo)

    # 2. Procura a receita correta pelo ID
    receita_encontrada = None
    for item in lista_receitas:
        if item["id"] == id:
            receita_encontrada = item
            break

    # 3. Se achou, mostra o template. Se não, erro 404 (básico)
    if receita_encontrada:
        return render_template("receita.html", receita=receita_encontrada)
    else:
        return "Receita não encontrada!", 404


if __name__ == "__main__":
    app.run(debug=True)
