from app.models.item import Item, TipoItem
from app.models.jogador import Jogador
from app.models.classe import TipoClasse
from app.services.inventario_service import InventarioService


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


def criar_item_teste() -> Item:
    return Item(
        id="espada-ferro",
        nome="Espada de Ferro",
        tipo=TipoItem.ARMA,
        descricao="Uma espada simples de ferro.",
        valor=50,
        quantidade=1
    )


def test_adicionar_item_ao_jogador():
    jogador = criar_jogador_teste()
    item = criar_item_teste()

    InventarioService.adicionar_item(
        jogador,
        item
    )

    assert len(jogador.inventario) == 1
    assert jogador.inventario[0].nome == "Espada de Ferro"


def test_remover_item_do_jogador():
    jogador = criar_jogador_teste()
    item = criar_item_teste()

    InventarioService.adicionar_item(
        jogador,
        item
    )

    InventarioService.remover_item(
        jogador,
        "espada-ferro"
    )

    assert jogador.inventario == []