from app.models.classe import TipoClasse
from app.models.equipamento import TipoArma
from app.models.slot_equipamento import TipoSlotEquipamento
from app.systems.equipamentos import EquipamentosSystem


def test_guerreiro_pode_equipar_espada():
    resultado = EquipamentosSystem.equipamento_permitido(
        TipoClasse.GUERREIRO,
        TipoSlotEquipamento.ARMA_DIREITA_1,
        TipoArma.ESPADA
    )

    assert resultado is True


def test_guerreiro_pode_equipar_escudo():
    resultado = EquipamentosSystem.equipamento_permitido(
        TipoClasse.GUERREIRO,
        TipoSlotEquipamento.ARMA_DIREITA_2,
        TipoArma.ESCUDO
    )

    assert resultado is True


def test_guerreiro_nao_pode_equipar_cajado():
    resultado = EquipamentosSystem.equipamento_permitido(
        TipoClasse.GUERREIRO,
        TipoSlotEquipamento.ARMA_DIREITA_1,
        TipoArma.CAJADO
    )

    assert resultado is False


def test_mago_pode_equipar_varinha():
    resultado = EquipamentosSystem.equipamento_permitido(
        TipoClasse.MAGO,
        TipoSlotEquipamento.ARMA_DIREITA_1,
        TipoArma.VARINHA
    )

    assert resultado is True


def test_mago_pode_equipar_foco():
    resultado = EquipamentosSystem.equipamento_permitido(
        TipoClasse.MAGO,
        TipoSlotEquipamento.ARMA_DIREITA_2,
        TipoArma.FOCO
    )

    assert resultado is True


def test_mago_nao_pode_equipar_espada():
    resultado = EquipamentosSystem.equipamento_permitido(
        TipoClasse.MAGO,
        TipoSlotEquipamento.ARMA_DIREITA_1,
        TipoArma.ESPADA
    )

    assert resultado is False


def test_ladino_pode_equipar_arco():
    resultado = EquipamentosSystem.equipamento_permitido(
        TipoClasse.LADINO,
        TipoSlotEquipamento.ARMA_ESQUERDA,
        TipoArma.ARCO
    )

    assert resultado is True


def test_ladino_pode_equipar_x_besta():
    resultado = EquipamentosSystem.equipamento_permitido(
        TipoClasse.LADINO,
        TipoSlotEquipamento.ARMA_ESQUERDA,
        TipoArma.XBesta
    )

    assert resultado is True


def test_ladino_pode_equipar_adaga():
    resultado = EquipamentosSystem.equipamento_permitido(
        TipoClasse.LADINO,
        TipoSlotEquipamento.ARMA_DIREITA_1,
        TipoArma.ADAGA
    )

    assert resultado is True


def test_ladino_nao_pode_equipar_cajado():
    resultado = EquipamentosSystem.equipamento_permitido(
        TipoClasse.LADINO,
        TipoSlotEquipamento.ARMA_ESQUERDA,
        TipoArma.CAJADO
    )

    assert resultado is False