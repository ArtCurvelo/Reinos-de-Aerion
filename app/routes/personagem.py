from flask import Blueprint, render_template

personagem = Blueprint("personagem", __name__)

@personagem.route("/novo-jogo")
def criar_personagem():
    return render_template("personagem/criacao.html")