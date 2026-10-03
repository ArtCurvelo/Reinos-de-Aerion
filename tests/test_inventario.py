from app.models.item import Item, TipoItem
from app.systems.inventario import InventarioSystem


def criar_item():
    return Item(
        id="espada-ferro",
        nome="Espada de Ferro",
        tipo=TipoItem.ARMA,
        descricao="Uma espada simples de ferro.",
        valor=25,
        quantidade=1
    )


def test_adicionar_item():
    inventario = []
    item = criar_item()

    InventarioSystem.adicionar_item(
        inventario,
        item
    )

    assert len(inventario) == 1
    assert inventario[0].id == "espada-ferro"
    assert inventario[0].quantidade == 1


def test_acumular_item():
    inventario = []

    InventarioSystem.adicionar_item(
        inventario,
        Item(
            id="pocao",
            nome="Poção",
            tipo=TipoItem.CONSUMIVEL,
            descricao="Recupera vida.",
            valor=10,
            quantidade=2
        )
    )

    InventarioSystem.adicionar_item(
        inventario,
        Item(
            id="pocao",
            nome="Poção",
            tipo=TipoItem.CONSUMIVEL,
            descricao="Recupera vida.",
            valor=10,
            quantidade=3
        )
    )

    assert len(inventario) == 1
    assert inventario[0].quantidade == 5


def test_remover_item():
    inventario = []

    InventarioSystem.adicionar_item(
        inventario,
        Item(
            id="pocao",
            nome="Poção",
            tipo=TipoItem.CONSUMIVEL,
            descricao="Recupera vida.",
            valor=10,
            quantidade=5
        )
    )

    InventarioSystem.remover_item(
        inventario,
        "pocao",
        2
    )

    assert inventario[0].quantidade == 3


def test_remover_item_completamente():
    inventario = []

    InventarioSystem.adicionar_item(
        inventario,
        criar_item()
    )

    InventarioSystem.remover_item(
        inventario,
        "espada-ferro"
    )

    assert len(inventario) == 0


def test_obter_item():
    inventario = []

    item = criar_item()

    InventarioSystem.adicionar_item(
        inventario,
        item
    )

    resultado = InventarioSystem.obter_item(
        inventario,
        "espada-ferro"
    )

    assert resultado is item


def test_item_nao_encontrado():
    inventario = []

    resultado = InventarioSystem.obter_item(
        inventario,
        "item-inexistente"
    )

    assert resultado is None