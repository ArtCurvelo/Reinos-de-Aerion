from flask import Blueprint, render_template, request, redirect, url_for, session

from app.models.classe import TipoClasse
from app.models.jogador import Jogador
from app.services.personagem_service import PersonagemService


personagem = Blueprint("personagem", __name__)


def jogador_para_dict(jogador: Jogador) -> dict:
    """
    Converte o jogador para um dicionário que pode ser
    armazenado na sessão do Flask.
    """

    return {
        "nome": jogador.nome,
        "classe": jogador.classe.value,
        "nivel": jogador.nivel,
        "experiencia": jogador.experiencia,
        "experiencia_maxima": jogador.experiencia_maxima,
        "ouro": jogador.ouro,

        "forca": jogador.forca,
        "destreza": jogador.destreza,
        "constituicao": jogador.constituicao,
        "inteligencia": jogador.inteligencia,
        "sabedoria": jogador.sabedoria,
        "carisma": jogador.carisma,

        "pontos_atributo": jogador.pontos_atributo
    }


def dict_para_jogador(dados: dict) -> Jogador:
    """
    Reconstrói um Jogador a partir dos dados armazenados
    na sessão.
    """

    return Jogador(
        nome=dados["nome"],
        classe=TipoClasse(dados["classe"]),

        nivel=dados["nivel"],
        experiencia=dados["experiencia"],
        experiencia_maxima=dados["experiencia_maxima"],
        ouro=dados["ouro"],

        forca=dados["forca"],
        destreza=dados["destreza"],
        constituicao=dados["constituicao"],
        inteligencia=dados["inteligencia"],
        sabedoria=dados["sabedoria"],
        carisma=dados["carisma"],

        pontos_atributo=dados["pontos_atributo"]
    )


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

        session["personagem_criacao"] = jogador_para_dict(jogador)

        print("PERSONAGEM CRIADO:")
        print(jogador)

        return redirect(
            url_for("personagem.distribuir_atributos")
        )

    return render_template("personagem/criacao.html")


@personagem.route("/novo-jogo/atributos")
def distribuir_atributos():

    jogador = session.get("personagem_criacao")

    if not jogador:
        return redirect(
            url_for("personagem.criar_personagem")
        )

    return render_template(
        "personagem/atributos.html",
        jogador=jogador
    )


@personagem.route(
    "/novo-jogo/atributos/aumentar",
    methods=["POST"]
)
def aumentar_atributo():

    dados = session.get("personagem_criacao")

    if not dados:
        return redirect(
            url_for("personagem.criar_personagem")
        )

    atributo = request.form.get("atributo")

    jogador = dict_para_jogador(dados)

    try:

        jogador = PersonagemService.aumentar_atributo(
            jogador,
            atributo
        )

    except ValueError as erro:

        print(f"ERRO AO AUMENTAR ATRIBUTO: {erro}")

        return redirect(
            url_for("personagem.distribuir_atributos")
        )

    session["personagem_criacao"] = jogador_para_dict(jogador)

    return redirect(
        url_for("personagem.distribuir_atributos")
    )


@personagem.route(
    "/novo-jogo/atributos/diminuir",
    methods=["POST"]
)
def diminuir_atributo():

    dados = session.get("personagem_criacao")

    if not dados:
        return redirect(
            url_for("personagem.criar_personagem")
        )

    atributo = request.form.get("atributo")

    jogador = dict_para_jogador(dados)

    try:

        jogador = PersonagemService.diminuir_atributo(
            jogador,
            atributo
        )

    except ValueError as erro:

        print(f"ERRO AO DIMINUIR ATRIBUTO: {erro}")

        return redirect(
            url_for("personagem.distribuir_atributos")
        )

    session["personagem_criacao"] = jogador_para_dict(jogador)

    return redirect(
        url_for("personagem.distribuir_atributos")
    )


@personagem.route(
    "/novo-jogo/atributos/confirmar",
    methods=["POST"]
)
def confirmar_atributos():

    dados = session.get("personagem_criacao")

    if not dados:
        return redirect(
            url_for("personagem.criar_personagem")
        )

    jogador = dict_para_jogador(dados)

    if jogador.pontos_atributo > 0:
        return redirect(
            url_for("personagem.distribuir_atributos")
        )

    session["jogador"] = jogador_para_dict(jogador)

    session.pop("personagem_criacao", None)

    print("PERSONAGEM CONFIRMADO:")
    print(jogador)

    return redirect(
        url_for("personagem.jogo")
    )


@personagem.route("/jogo")
def jogo():

    jogador = session.get("jogador")

    print("DADOS DA SESSÃO:")
    print(jogador)

    if not jogador:
        return redirect(
            url_for("personagem.criar_personagem")
        )

    return render_template(
        "jogo/index.html",
        jogador=jogador
    )