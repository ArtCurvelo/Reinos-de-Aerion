from app.models.classe import TipoClasse
from app.models.equipamento import (
    Equipamento,
    TipoArma,
    TipoEquipamento
)
from app.models.jogador import Jogador
from app.models.slot_equipamento import TipoSlotEquipamento
from app.models.equipamentos_equipados import EquipamentosEquipados
from app.services.equipamentos_service import EquipamentosService
from app.services.inventario_service import InventarioService


def criar_jogador_teste() -> Jogador:
    return Jogador(
        nome="Arthur",
        classe=TipoClasse.GUERREIRO,
        forca=15,
        destreza=12,
        constituicao=14,
        inteligencia=8,
        sabedoria=10,
        carisma=10
    )


def criar_espada_teste() -> Equipamento:
    return Equipamento(
        id="espada-ferro",
        nome="Espada de Ferro",
        tipo=TipoEquipamento.ARMA,
        descricao="Uma espada simples de ferro.",
        valor=50,
        tipo_arma=TipoArma.ESPADA
    )


def test_equipar_espada():

    jogador = criar_jogador_teste()
    espada = criar_espada_teste()
    equipamentos = EquipamentosEquipados()

    InventarioService.adicionar_item(
        jogador,
        espada
    )

    EquipamentosService.equipar(
        jogador,
        equipamentos,
        espada,
        TipoSlotEquipamento.ARMA_DIREITA_1
    )

    assert (
        equipamentos.slots[
            TipoSlotEquipamento.ARMA_DIREITA_1
        ] == espada
    )


def test_nao_pode_equipar_arma_incompativel():

    jogador = criar_jogador_teste()

    cajado = Equipamento(
        id="cajado-madeira",
        nome="Cajado de Madeira",
        tipo=TipoEquipamento.ARMA,
        descricao="Um cajado simples.",
        valor=60,
        tipo_arma=TipoArma.CAJADO
    )

    equipamentos = EquipamentosEquipados()

    try:
        EquipamentosService.equipar(
            jogador,
            equipamentos,
            cajado,
            TipoSlotEquipamento.ARMA_DIREITA_1
        )
        assert False
    except ValueError:
        assert True