from app.models.item import Item


class InventarioSystem:

    @staticmethod
    def adicionar_item(
        inventario: list[Item],
        item: Item
    ) -> list[Item]:

        for item_existente in inventario:

            if item_existente.id == item.id:

                item_existente.quantidade += item.quantidade

                return inventario

        inventario.append(item)

        return inventario

    @staticmethod
    def remover_item(
        inventario: list[Item],
        item_id: str,
        quantidade: int = 1
    ) -> list[Item]:

        if quantidade <= 0:
            raise ValueError(
                "A quantidade deve ser maior que zero."
            )

        for item in inventario:

            if item.id == item_id:

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
        inventario: list[Item],
        item_id: str
    ) -> Item | None:

        for item in inventario:

            if item.id == item_id:
                return item

        return None