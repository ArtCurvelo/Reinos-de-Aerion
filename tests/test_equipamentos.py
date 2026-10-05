from app.models.classe import TipoClasse
from app.models.equipamento import TipoArma
from app.models.slot_equipamento import TipoSlotEquipamento
from app.systems.equipamentos import EquipamentosSystem


def test_obter_configuracoes_do_guerreiro():
    configuracoes = EquipamentosSystem.obter_configuracoes(
        TipoClasse.GUERREIRO
    )

    assert len(configuracoes) == 5


def test_guerreiro_pode_usar_espada_e_escudo():
    configuracoes = EquipamentosSystem.obter_configuracoes(
        TipoClasse.GUERREIRO
    )

    configuracao = configuracoes[0]

    assert configuracao.nome == "Espada + Escudo"

    assert configuracao.armas[0].slot == TipoSlotEquipamento.ARMA_DIREITA_1
    assert configuracao.armas[0].tipos == [TipoArma.ESPADA]

    assert configuracao.armas[1].slot == TipoSlotEquipamento.ARMA_DIREITA_2
    assert configuracao.armas[1].tipos == [TipoArma.ESCUDO]


def test_guerreiro_pode_usar_espada_sem_escudo():
    configuracoes = EquipamentosSystem.obter_configuracoes(
        TipoClasse.GUERREIRO
    )

    configuracao = configuracoes[2]

    assert configuracao.nome == "Espada"
    assert len(configuracao.armas) == 1
    assert configuracao.armas[0].tipos == [TipoArma.ESPADA]


def test_guerreiro_pode_usar_espadão():
    configuracoes = EquipamentosSystem.obter_configuracoes(
        TipoClasse.GUERREIRO
    )

    configuracao = configuracoes[4]

    assert configuracao.nome == "Espadão"
    assert len(configuracao.armas) == 1
    assert configuracao.armas[0].tipos == [TipoArma.ESPADAO]