from app.models.equipamentos_equipados import EquipamentosEquipados
from app.models.slot_equipamento import TipoSlotEquipamento


def test_criar_equipamentos_equipados():
    equipamentos = EquipamentosEquipados()

    assert len(equipamentos.slots) == 11


def test_slots_comecam_vazios():
    equipamentos = EquipamentosEquipados()

    for equipamento in equipamentos.slots.values():
        assert equipamento is None


def test_slot_de_arma_comeca_vazio():
    equipamentos = EquipamentosEquipados()

    assert (
        equipamentos.slots[
            TipoSlotEquipamento.ARMA_DIREITA_1
        ] is None
    )
