from app.systems.atributos import AtributosSystem


def test_custo_atributo_abaixo_de_15():
    assert AtributosSystem.custo_aumento(14) == 1


def test_custo_atributo_a_partir_de_15():
    assert AtributosSystem.custo_aumento(15) == 2


def test_atributo_pode_ser_aumentado():
    assert AtributosSystem.pode_aumentar(14) is True


def test_atributo_nao_pode_passar_de_20():
    assert AtributosSystem.pode_aumentar(20) is False


def test_aumentar_atributo():
    novo_valor, pontos_restantes = AtributosSystem.aumentar(14, 3)

    assert novo_valor == 15
    assert pontos_restantes == 2


def test_aumentar_atributo_acima_de_15():
    novo_valor, pontos_restantes = AtributosSystem.aumentar(15, 3)

    assert novo_valor == 16
    assert pontos_restantes == 1


def test_modificador():
    assert AtributosSystem.modificador(8) == -1
    assert AtributosSystem.modificador(10) == 0
    assert AtributosSystem.modificador(14) == 2
    assert AtributosSystem.modificador(16) == 3
    assert AtributosSystem.modificador(20) == 5