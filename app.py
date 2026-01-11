import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    with open("dados.json", encoding="utf-8") as arquivo:
        lista_receitas = json.load(arquivo)

    return render_template("index.html", receitas=lista_receitas)


if __name__ == "__main__":
    app.run(debug=True)
