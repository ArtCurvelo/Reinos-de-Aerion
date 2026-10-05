from app.models.equipamento import Equipamento
from app.models.item import Item


class InventarioSystem:

    @staticmethod
    def adicionar_item(
        inventario: list[Item | Equipamento],
        item: Item | Equipamento
    ) -> list[Item | Equipamento]:

        # Equipamentos não são empilháveis.
        if isinstance(item, Equipamento):
            inventario.append(item)
            return inventario

        # Itens comuns podem ser empilhados.
        for item_existente in inventario:

            if (
                isinstance(item_existente, Item)
                and item_existente.id == item.id
            ):
                item_existente.quantidade += item.quantidade
                return inventario

        inventario.append(item)

        return inventario

    @staticmethod
    def remover_item(
        inventario: list[Item | Equipamento],
        item_id: str,
        quantidade: int = 1
    ) -> list[Item | Equipamento]:

        if quantidade <= 0:
            raise ValueError(
                "A quantidade deve ser maior que zero."
            )

        for item in inventario:

            if item.id != item_id:
                continue

            # Equipamentos são unidades individuais.
            if isinstance(item, Equipamento):

                if quantidade != 1:
                    raise ValueError(
                        "Equipamentos não podem ser removidos em quantidade."
                    )

                inventario.remove(item)

                return inventario

            # Itens empilháveis.
            if item.quantidade < quantidade:
                raise ValueError(
                    "Quantidade insuficiente no inventário."
                )

            item.quantidade -= quantidade

            if item.quantidade == 0:
                inventario.remove(item)

            return inventario

        raise ValueError(
            "Item não encontrado no inventário."
        )

    @staticmethod
    def obter_item(
        inventario: list[Item | Equipamento],
        item_id: str
    ) -> Item | Equipamento | None:

        for item in inventario:

            if item.id == item_id:
                return item

        return None