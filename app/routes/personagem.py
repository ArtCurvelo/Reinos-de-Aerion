from flask import Blueprint, render_template, request

from app.models.classe import TipoClasse
from app.services.personagem_service import PersonagemService


personagem = Blueprint("personagem", __name__)


@personagem.route("/novo-jogo", methods=["GET", "POST"])
def criar_personagem():

    if request.method == "POST":

        nome = request.form.get("nome")
        classe = request.form.get("classe")

        tipo_classe = TipoClasse(classe)

        jogador = PersonagemService.criar_jogador(
            nome,
            tipo_classe
        )

        print(jogador)

    return render_template("personagem/criacao.html")