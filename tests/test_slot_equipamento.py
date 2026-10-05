from app.models.slot_equipamento import TipoSlotEquipamento


def test_slots_de_armas():
    assert TipoSlotEquipamento.ARMA_ESQUERDA.value == "Arma Esquerda"
    assert TipoSlotEquipamento.ARMA_DIREITA_1.value == "Arma Direita 1"
    assert TipoSlotEquipamento.ARMA_DIREITA_2.value == "Arma Direita 2"


def test_slots_de_armadura():
    assert TipoSlotEquipamento.CABECA.value == "Cabeça"
    assert TipoSlotEquipamento.PEITORAL.value == "Peitoral"
    assert TipoSlotEquipamento.LUVAS.value == "Luvas"
    assert TipoSlotEquipamento.CALCAS.value == "Calças"
    assert TipoSlotEquipamento.BOTAS.value == "Botas"


def test_slots_de_acessorios():
    assert TipoSlotEquipamento.ACESSORIO_1.value == "Acessório 1"
    assert TipoSlotEquipamento.ACESSORIO_2.value == "Acessório 2"
    assert TipoSlotEquipamento.ACESSORIO_3.value == "Acessório 3"