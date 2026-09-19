from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    #dados que serão calculados pelo Python
    Titulo_pagina = "Dashboard de Demonstração"
    Aluno = {"nome": "Vitinho", "curso": "Analista de Sistemas", "nota": "9.5"}
    Status = "Aprovado" if Aluno["nota"] >= 7 else "Reprovado"

    return render_template(
    "index.html",
    titulo=Titulo_pagina,
    aluno=Aluno,
    usuario=Aluno,
    resultado=Status
    )

if __name__ == "__main__":
    app.run(debug=True)          