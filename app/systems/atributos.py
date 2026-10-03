class AtributosSystem:

    VALOR_MINIMO = 8
    VALOR_MAXIMO = 20

    @staticmethod
    def custo_aumento(valor_atual: int) -> int:
        """
        Retorna quantos pontos são necessários
        para aumentar um atributo em 1.
        """

        if valor_atual < 15:
            return 1

        return 2

    @staticmethod
    def pode_aumentar(valor_atual: int) -> bool:
        """
        Verifica se o atributo ainda pode ser aumentado.
        """

        return valor_atual < AtributosSystem.VALOR_MAXIMO

    @staticmethod
    def pode_diminuir(valor_atual: int) -> bool:
        """
        Verifica se o atributo ainda pode ser diminuído.
        """

        return valor_atual > AtributosSystem.VALOR_MINIMO

    @staticmethod
    def aumentar(
        valor_atual: int,
        pontos_disponiveis: int
    ):
        """
        Tenta aumentar um atributo em 1 ponto.

        Retorna:
        - novo valor do atributo
        - pontos restantes
        """

        if not AtributosSystem.pode_aumentar(valor_atual):
            raise ValueError(
                "O atributo já atingiu o valor máximo."
            )

        custo = AtributosSystem.custo_aumento(
            valor_atual
        )

        if pontos_disponiveis < custo:
            raise ValueError(
                "Pontos de atributo insuficientes."
            )

        novo_valor = valor_atual + 1
        pontos_restantes = pontos_disponiveis - custo

        return novo_valor, pontos_restantes

    @staticmethod
    def diminuir(valor_atual: int):
        """
        Diminui um atributo em 1 ponto e devolve
        os pontos utilizados para esse aumento.

        Retorna:
        - novo valor do atributo
        - pontos devolvidos
        """

        if not AtributosSystem.pode_diminuir(valor_atual):
            raise ValueError(
                "O atributo já atingiu o valor mínimo."
            )

        custo = AtributosSystem.custo_aumento(
            valor_atual - 1
        )

        novo_valor = valor_atual - 1

        return novo_valor, custo

    @staticmethod
    def modificador(valor: int) -> int:
        """
        Calcula o modificador de um atributo.
        """

        return (valor - 10) // 2