from app.models.equipamento import (
    Equipamento,
    TipoArma,
    TipoEquipamento,
)


def test_criar_espada():
    espada = Equipamento(
        id="espada-ferro",
        nome="Espada de Ferro",
        tipo=TipoEquipamento.ARMA,
        descricao="Uma espada simples de ferro.",
        valor=50,
        tipo_arma=TipoArma.ESPADA,
        maos=1,
        nivel_requerido=1,
        forca=2,
    )

    assert espada.nome == "Espada de Ferro"
    assert espada.tipo == TipoEquipamento.ARMA
    assert espada.tipo_arma == TipoArma.ESPADA
    assert espada.maos == 1
    assert espada.forca == 2


def test_criar_espadão():
    espadao = Equipamento(
        id="espadao-ferro",
        nome="Espadão de Ferro",
        tipo=TipoEquipamento.ARMA,
        descricao="Uma grande espada de duas mãos.",
        valor=100,
        tipo_arma=TipoArma.ESPADAO,
        maos=2,
        nivel_requerido=5,
        forca=5,
    )

    assert espadao.tipo_arma == TipoArma.ESPADAO
    assert espadao.maos == 2
    assert espadao.nivel_requerido == 5


def test_criar_armadura():
    armadura = Equipamento(
        id="peitoral-ferro",
        nome="Peitoral de Ferro",
        tipo=TipoEquipamento.ARMADURA,
        descricao="Um peitoral resistente de ferro.",
        valor=80,
        nivel_requerido=3,
        constituicao=4,
    )

    assert armadura.tipo == TipoEquipamento.ARMADURA
    assert armadura.constituicao == 4


def test_criar_acessorio():
    acessorio = Equipamento(
        id="anel-forca",
        nome="Anel da Força",
        tipo=TipoEquipamento.ACESSORIO,
        descricao="Um anel que aumenta a força.",
        valor=120,
        nivel_requerido=2,
        forca=3,
    )

    assert acessorio.tipo == TipoEquipamento.ACESSORIO
    assert acessorio.forca == 3

def test_tipos_de_armas():
    assert TipoArma.ESCUDO.value == "Escudo"
    assert TipoArma.ARCO.value == "Arco"
    assert TipoArma.XBesta.value == "X-Besta"
    assert TipoArma.ADAGA.value == "Adaga"
    assert TipoArma.VARINHA.value == "Varinha"
    assert TipoArma.FOCO.value == "Foco"
    assert TipoArma.CAJADO.value == "Cajado"