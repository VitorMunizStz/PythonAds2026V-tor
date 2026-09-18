from flask import flask

app = Flask(__name__)

app.route("/")
def home():
    #dados que serão calculados pelo Python
    titulo_pagina = "Dashboard de Demonstração"
    aluno = {"nome": "Vitinho", "curso": "Analista de Sistemas", "nota": "9.5"}
    status = "Aprovado" if aluno["nota"] >= 7 else "Reprovado"
    
    return render_template(
    "index.html",
    titulo=titulo_pagina,
    aluno=aluno,
    usuario=aluno,
    resultado=status
    )

if __name__ == "__main__":
    app.run(debug=True)          