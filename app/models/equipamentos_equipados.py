from app.models.equipamento import Equipamento
from app.models.slot_equipamento import TipoSlotEquipamento


class EquipamentosEquipados:
    def __init__(self):
        self.slots: dict[
            TipoSlotEquipamento,
            Equipamento | None
        ] = {
            slot: None
            for slot in TipoSlotEquipamento
        }