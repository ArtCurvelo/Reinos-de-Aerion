from flask import Blueprint, render_template, request, redirect, url_for, session

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

        session["jogador"] = {
            "nome": jogador.nome,
            "classe": jogador.classe.value,
            "nivel": jogador.nivel,
            "experiencia": jogador.experiencia,
            "experiencia_maxima": jogador.experiencia_maxima,
            "ouro": jogador.ouro,

            "vida": jogador.vida,
            "vida_maxima": jogador.vida_maxima,

            "mana": jogador.mana,
            "mana_maxima": jogador.mana_maxima,

            "forca": jogador.forca,
            "inteligencia": jogador.inteligencia,
            "destreza": jogador.destreza,

            "vida_porcentagem": (
                jogador.vida / jogador.vida_maxima
            ) * 100,

            "mana_porcentagem": (
                jogador.mana / jogador.mana_maxima
            ) * 100
        }

        print(jogador)

        return redirect(url_for("personagem.jogo"))

    return render_template("personagem/criacao.html")


@personagem.route("/jogo")
def jogo():

    jogador = session.get("jogador")

    print("DADOS DA SESSÃO:")
    print(jogador)

    if not jogador:
        return redirect(url_for("personagem.criar_personagem"))

    return render_template(
        "jogo/index.html",
        jogador=jogador
    )