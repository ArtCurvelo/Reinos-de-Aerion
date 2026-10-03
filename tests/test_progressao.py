from app.models.classe import TipoClasse
from app.models.jogador import Jogador
from app.systems.progressao import ProgressaoSystem


def criar_jogador_teste():
    return Jogador(
        nome="Teste",
        classe=TipoClasse.GUERREIRO,

        forca=14,
        destreza=10,
        constituicao=14,
        inteligencia=8,
        sabedoria=10,
        carisma=8
    )


def test_experiencia_proximo_nivel():
    assert ProgressaoSystem.experiencia_proximo_nivel(1) == 100
    assert ProgressaoSystem.experiencia_proximo_nivel(2) == 170
    assert ProgressaoSystem.experiencia_proximo_nivel(3) == 289


def test_adicionar_experiencia_sem_subir_nivel():

    jogador = criar_jogador_teste()

    ProgressaoSystem.adicionar_experiencia(
        jogador,
        50
    )

    assert jogador.nivel == 1
    assert jogador.experiencia == 50
    assert jogador.experiencia_maxima == 100
    assert jogador.pontos_habilidade == 0


def test_subir_nivel():

    jogador = criar_jogador_teste()

    ProgressaoSystem.adicionar_experiencia(
        jogador,
        100
    )

    assert jogador.nivel == 2
    assert jogador.experiencia == 0
    assert jogador.experiencia_maxima == 170
    assert jogador.pontos_habilidade == 1


def test_manter_experiencia_excedente():

    jogador = criar_jogador_teste()

    ProgressaoSystem.adicionar_experiencia(
        jogador,
        130
    )

    assert jogador.nivel == 2
    assert jogador.experiencia == 30
    assert jogador.experiencia_maxima == 170
    assert jogador.pontos_habilidade == 1


def test_multiplos_niveis():

    jogador = criar_jogador_teste()

    ProgressaoSystem.adicionar_experiencia(
        jogador,
        500
    )

    assert jogador.nivel == 3
    assert jogador.experiencia == 230
    assert jogador.experiencia_maxima == 289
    assert jogador.pontos_habilidade == 2


def test_nivel_maximo():

    jogador = criar_jogador_teste()

    jogador.nivel = 20
    jogador.experiencia = 0
    jogador.experiencia_maxima = 0

    ProgressaoSystem.adicionar_experiencia(
        jogador,
        10000
    )

    assert jogador.nivel == 20
    assert jogador.experiencia == 0