from app.models.classe import TipoClasse
from app.models.jogador import Jogador
from app.models.item import Item, TipoItem


def criar_jogador_teste() -> Jogador:
    return Jogador(
        nome="Arthur",
        classe=TipoClasse.GUERREIRO,
        forca=15,
        destreza=12,
        constituicao=14,
        inteligencia=8,
        sabedoria=10,
        carisma=10
    )


def test_jogador_comeca_com_inventario_vazio():
    jogador = criar_jogador_teste()

    assert jogador.inventario == []


def test_jogadores_possuem_inventarios_independentes():
    jogador1 = criar_jogador_teste()
    jogador2 = criar_jogador_teste()

    item = Item(
        id="espada-ferro",
        nome="Espada de Ferro",
        tipo=TipoItem.ARMA,
        descricao="Uma espada simples de ferro.",
        valor=50,
        quantidade=1
    )

    jogador1.inventario.append(item)

    assert len(jogador1.inventario) == 1
    assert len(jogador2.inventario) == 0