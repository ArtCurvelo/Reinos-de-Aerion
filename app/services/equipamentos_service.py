from app.models.equipamento import Equipamento
from app.models.jogador import Jogador
from app.models.slot_equipamento import TipoSlotEquipamento
from app.models.equipamentos_equipados import EquipamentosEquipados
from app.systems.equipamentos import EquipamentosSystem
from app.systems.inventario import InventarioSystem


class EquipamentosService:

    @staticmethod
    def equipar(
        jogador: Jogador,
        equipamentos_equipados: EquipamentosEquipados,
        item: Equipamento,
        slot: TipoSlotEquipamento
    ) -> EquipamentosEquipados:

        item_no_inventario = next(
            (
                item_inventario
                for item_inventario in jogador.inventario
                if item_inventario.id == item.id
            ),
            None
        )

        if item_no_inventario is None:
            raise ValueError(
                "O equipamento não está no inventário."
            )

        if not EquipamentosSystem.equipamento_permitido(
            jogador.classe,
            slot,
            item.tipo_arma
        ):
            raise ValueError(
                "Esse equipamento não pode ser equipado nesse slot."
            )

        if equipamentos_equipados.slots[slot] is not None:
            raise ValueError(
                "Esse slot já está ocupado."
            )

        InventarioSystem.remover_item(
            jogador.inventario,
            item.id
        )

        equipamentos_equipados.slots[slot] = item

        return equipamentos_equipados

    @staticmethod
    def desequipar(
        jogador: Jogador,
        equipamentos_equipados: EquipamentosEquipados,
        slot: TipoSlotEquipamento
    ) -> EquipamentosEquipados:

        equipamento = equipamentos_equipados.slots[slot]

        if equipamento is None:
            raise ValueError(
                "Não existe equipamento nesse slot."
            )

        InventarioSystem.adicionar_item(
            jogador.inventario,
            equipamento
        )

        equipamentos_equipados.slots[slot] = None

        return equipamentos_equipados