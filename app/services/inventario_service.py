from app.models.item import Item
from app.models.jogador import Jogador
from app.systems.inventario import InventarioSystem


class InventarioService:

    @staticmethod
    def adicionar_item(
        jogador: Jogador,
        item: Item
    ) -> Jogador:

        InventarioSystem.adicionar_item(
            jogador.inventario,
            item
        )

        return jogador

    @staticmethod
    def remover_item(
        jogador: Jogador,
        item_id: str,
        quantidade: int = 1
    ) -> Jogador:

        InventarioSystem.remover_item(
            jogador.inventario,
            item_id,
            quantidade
        )

        return jogador

    @staticmethod
    def obter_item(
        jogador: Jogador,
        item_id: str
    ) -> Item | None:

        return InventarioSystem.obter_item(
            jogador.inventario,
            item_id
        )