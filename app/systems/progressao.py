class ProgressaoSystem:

    NIVEL_MAXIMO = 20
    XP_BASE = 100
    MULTIPLICADOR_XP = 1.7

    @staticmethod
    def experiencia_proximo_nivel(nivel: int) -> int:
        """
        Calcula a experiência necessária para passar
        do nível atual para o próximo.

        A fórmula é:

        XP = 100 * (1.7 ** (nível - 1))

        O nível 20 é o nível máximo e não possui
        próximo nível.
        """

        if nivel >= ProgressaoSystem.NIVEL_MAXIMO:
            return 0

        experiencia = (
            ProgressaoSystem.XP_BASE
            * (
                ProgressaoSystem.MULTIPLICADOR_XP
                ** (nivel - 1)
            )
        )

        return round(experiencia)

    @staticmethod
    def adicionar_experiencia(
        jogador,
        quantidade: int
    ):
        """
        Adiciona experiência ao jogador e processa
        todos os níveis obtidos.

        O XP excedente permanece após o level-up.
        """

        if quantidade < 0:
            raise ValueError(
                "A quantidade de experiência não pode ser negativa."
            )

        if jogador.nivel >= ProgressaoSystem.NIVEL_MAXIMO:
            return jogador

        jogador.experiencia += quantidade

        while (
            jogador.nivel < ProgressaoSystem.NIVEL_MAXIMO
            and jogador.experiencia >= jogador.experiencia_maxima
        ):

            jogador.experiencia -= jogador.experiencia_maxima

            jogador.nivel += 1

            # Recompensa básica por subir de nível.
            jogador.pontos_habilidade += 1

            jogador.experiencia_maxima = (
                ProgressaoSystem.experiencia_proximo_nivel(
                    jogador.nivel
                )
            )

        return jogador