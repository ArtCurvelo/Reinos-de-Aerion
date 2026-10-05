import pytest

from app.models.classe import TipoClasse
from app.models.equipamento import (
    Equipamento,
    TipoArma,
    TipoEquipamento
)
from app.models.equipamentos_equipados import EquipamentosEquipados
from app.models.jogador import Jogador
from app.models.slot_equipamento import TipoSlotEquipamento
from app.services.equipamentos_service import EquipamentosService
from app.services.inventario_service import InventarioService


def criar_jogador(
    classe: TipoClasse = TipoClasse.GUERREIRO
) -> Jogador:
    return Jogador(
        nome="Arthur",
        classe=classe,
        forca=15,
        destreza=12,
        constituicao=14,
        inteligencia=8,
        sabedoria=10,
        carisma=10
    )


def criar_espada() -> Equipamento:
    return Equipamento(
        id="espada-ferro",
        nome="Espada de Ferro",
        tipo=TipoEquipamento.ARMA,
        descricao="Uma espada simples de ferro.",
        valor=50,
        tipo_arma=TipoArma.ESPADA
    )


def criar_escudo() -> Equipamento:
    return Equipamento(
        id="escudo-ferro",
        nome="Escudo de Ferro",
        tipo=TipoEquipamento.ARMA,
        descricao="Um escudo resistente de ferro.",
        valor=60,
        tipo_arma=TipoArma.ESCUDO
    )


def criar_cajado() -> Equipamento:
    return Equipamento(
        id="cajado-madeira",
        nome="Cajado de Madeira",
        tipo=TipoEquipamento.ARMA,
        descricao="Um cajado simples de madeira.",
        valor=70,
        tipo_arma=TipoArma.CAJADO,
        maos=2
    )


def criar_varinha() -> Equipamento:
    return Equipamento(
        id="varinha-madeira",
        nome="Varinha de Madeira",
        tipo=TipoEquipamento.ARMA,
        descricao="Uma varinha simples.",
        valor=40,
        tipo_arma=TipoArma.VARINHA
    )


def criar_foco() -> Equipamento:
    return Equipamento(
        id="foco-cristal",
        nome="Foco de Cristal",
        tipo=TipoEquipamento.ARMA,
        descricao="Um foco mágico de cristal.",
        valor=50,
        tipo_arma=TipoArma.FOCO
    )


def criar_arco() -> Equipamento:
    return Equipamento(
        id="arco-madeira",
        nome="Arco de Madeira",
        tipo=TipoEquipamento.ARMA,
        descricao="Um arco simples.",
        valor=45,
        tipo_arma=TipoArma.ARCO
    )


def criar_adaga() -> Equipamento:
    return Equipamento(
        id="adaga-ferro",
        nome="Adaga de Ferro",
        tipo=TipoEquipamento.ARMA,
        descricao="Uma adaga simples.",
        valor=35,
        tipo_arma=TipoArma.ADAGA
    )


def test_equipar_e_desequipar_espada():

    jogador = criar_jogador()
    espada = criar_espada()
    equipamentos = EquipamentosEquipados()

    InventarioService.adicionar_item(
        jogador,
        espada
    )

    assert len(jogador.inventario) == 1

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

    assert (
        InventarioService.obter_item(
            jogador,
            espada.id
        ) is None
    )

    EquipamentosService.desequipar(
        jogador,
        equipamentos,
        TipoSlotEquipamento.ARMA_DIREITA_1
    )

    assert (
        equipamentos.slots[
            TipoSlotEquipamento.ARMA_DIREITA_1
        ] is None
    )

    assert (
        InventarioService.obter_item(
            jogador,
            espada.id
        ) is not None
    )


def test_guerreiro_pode_equipar_espada_e_escudo():

    jogador = criar_jogador()
    espada = criar_espada()
    escudo = criar_escudo()
    equipamentos = EquipamentosEquipados()

    InventarioService.adicionar_item(jogador, espada)
    InventarioService.adicionar_item(jogador, escudo)

    EquipamentosService.equipar(
        jogador,
        equipamentos,
        espada,
        TipoSlotEquipamento.ARMA_DIREITA_1
    )

    EquipamentosService.equipar(
        jogador,
        equipamentos,
        escudo,
        TipoSlotEquipamento.ARMA_DIREITA_2
    )

    assert (
        equipamentos.slots[
            TipoSlotEquipamento.ARMA_DIREITA_1
        ] == espada
    )

    assert (
        equipamentos.slots[
            TipoSlotEquipamento.ARMA_DIREITA_2
        ] == escudo
    )

    assert jogador.inventario == []


def test_nao_pode_equipar_item_fora_do_inventario():

    jogador = criar_jogador()
    espada = criar_espada()
    equipamentos = EquipamentosEquipados()

    with pytest.raises(ValueError):
        EquipamentosService.equipar(
            jogador,
            equipamentos,
            espada,
            TipoSlotEquipamento.ARMA_DIREITA_1
        )


def test_nao_pode_equipar_arma_incompativel():

    jogador = criar_jogador()
    cajado = criar_cajado()
    equipamentos = EquipamentosEquipados()

    InventarioService.adicionar_item(
        jogador,
        cajado
    )

    with pytest.raises(ValueError):
        EquipamentosService.equipar(
            jogador,
            equipamentos,
            cajado,
            TipoSlotEquipamento.ARMA_DIREITA_1
        )

    assert (
        InventarioService.obter_item(
            jogador,
            cajado.id
        ) is not None
    )


def test_nao_pode_equipar_em_slot_ocupado():

    jogador = criar_jogador()
    espada = criar_espada()
    outra_espada = Equipamento(
        id="espada-ferro-2",
        nome="Espada de Ferro 2",
        tipo=TipoEquipamento.ARMA,
        descricao="Outra espada simples.",
        valor=50,
        tipo_arma=TipoArma.ESPADA
    )

    equipamentos = EquipamentosEquipados()

    InventarioService.adicionar_item(jogador, espada)
    InventarioService.adicionar_item(jogador, outra_espada)

    EquipamentosService.equipar(
        jogador,
        equipamentos,
        espada,
        TipoSlotEquipamento.ARMA_DIREITA_1
    )

    with pytest.raises(ValueError):
        EquipamentosService.equipar(
            jogador,
            equipamentos,
            outra_espada,
            TipoSlotEquipamento.ARMA_DIREITA_1
        )


def test_nao_pode_desequipar_slot_vazio():

    jogador = criar_jogador()
    equipamentos = EquipamentosEquipados()

    with pytest.raises(ValueError):
        EquipamentosService.desequipar(
            jogador,
            equipamentos,
            TipoSlotEquipamento.ARMA_DIREITA_1
        )


def test_mago_pode_equipar_varinha_e_foco():

    jogador = criar_jogador(TipoClasse.MAGO)

    varinha = criar_varinha()
    foco = criar_foco()

    equipamentos = EquipamentosEquipados()

    InventarioService.adicionar_item(jogador, varinha)
    InventarioService.adicionar_item(jogador, foco)

    EquipamentosService.equipar(
        jogador,
        equipamentos,
        varinha,
        TipoSlotEquipamento.ARMA_DIREITA_1
    )

    EquipamentosService.equipar(
        jogador,
        equipamentos,
        foco,
        TipoSlotEquipamento.ARMA_DIREITA_2
    )

    assert (
        equipamentos.slots[
            TipoSlotEquipamento.ARMA_DIREITA_1
        ] == varinha
    )

    assert (
        equipamentos.slots[
            TipoSlotEquipamento.ARMA_DIREITA_2
        ] == foco
    )

    assert jogador.inventario == []


def test_ladino_pode_equipar_arco_e_duas_adagas():

    jogador = criar_jogador(TipoClasse.LADINO)

    arco = criar_arco()
    adaga_1 = criar_adaga()
    adaga_2 = Equipamento(
        id="adaga-ferro-2",
        nome="Adaga de Ferro 2",
        tipo=TipoEquipamento.ARMA,
        descricao="Uma segunda adaga simples.",
        valor=35,
        tipo_arma=TipoArma.ADAGA
    )

    equipamentos = EquipamentosEquipados()

    InventarioService.adicionar_item(jogador, arco)
    InventarioService.adicionar_item(jogador, adaga_1)
    InventarioService.adicionar_item(jogador, adaga_2)

    EquipamentosService.equipar(
        jogador,
        equipamentos,
        arco,
        TipoSlotEquipamento.ARMA_ESQUERDA
    )

    EquipamentosService.equipar(
        jogador,
        equipamentos,
        adaga_1,
        TipoSlotEquipamento.ARMA_DIREITA_1
    )

    EquipamentosService.equipar(
        jogador,
        equipamentos,
        adaga_2,
        TipoSlotEquipamento.ARMA_DIREITA_2
    )

    assert (
        equipamentos.slots[
            TipoSlotEquipamento.ARMA_ESQUERDA
        ] == arco
    )

    assert (
        equipamentos.slots[
            TipoSlotEquipamento.ARMA_DIREITA_1
        ] == adaga_1
    )

    assert (
        equipamentos.slots[
            TipoSlotEquipamento.ARMA_DIREITA_2
        ] == adaga_2
    )

    assert jogador.inventario == []


def test_desequipar_devolve_item_ao_inventario():

    jogador = criar_jogador()
    espada = criar_espada()
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

    EquipamentosService.desequipar(
        jogador,
        equipamentos,
        TipoSlotEquipamento.ARMA_DIREITA_1
    )

    item = InventarioService.obter_item(
        jogador,
        espada.id
    )

    assert item is not None
    assert item.id == espada.id
    assert item == espada