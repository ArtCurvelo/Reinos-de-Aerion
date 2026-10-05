from app.models.classe import TipoClasse
from app.models.configuracao_arma import ArmaPermitida, ConfiguracaoArma
from app.models.equipamento import TipoArma
from app.models.slot_equipamento import TipoSlotEquipamento


class EquipamentosSystem:

    CONFIGURACOES = {
        TipoClasse.GUERREIRO: [
            ConfiguracaoArma(
                nome="Espada + Escudo",
                armas=[
                    ArmaPermitida(
                        slot=TipoSlotEquipamento.ARMA_DIREITA_1,
                        tipos=[TipoArma.ESPADA]
                    ),
                    ArmaPermitida(
                        slot=TipoSlotEquipamento.ARMA_DIREITA_2,
                        tipos=[TipoArma.ESCUDO]
                    )
                ]
            ),
            ConfiguracaoArma(
                nome="Maça + Escudo",
                armas=[
                    ArmaPermitida(
                        slot=TipoSlotEquipamento.ARMA_DIREITA_1,
                        tipos=[TipoArma.MACA]
                    ),
                    ArmaPermitida(
                        slot=TipoSlotEquipamento.ARMA_DIREITA_2,
                        tipos=[TipoArma.ESCUDO]
                    )
                ]
            ),
            ConfiguracaoArma(
                nome="Espada",
                armas=[
                    ArmaPermitida(
                        slot=TipoSlotEquipamento.ARMA_DIREITA_1,
                        tipos=[TipoArma.ESPADA]
                    )
                ]
            ),
            ConfiguracaoArma(
                nome="Maça",
                armas=[
                    ArmaPermitida(
                        slot=TipoSlotEquipamento.ARMA_DIREITA_1,
                        tipos=[TipoArma.MACA]
                    )
                ]
            ),
            ConfiguracaoArma(
                nome="Espadão",
                armas=[
                    ArmaPermitida(
                        slot=TipoSlotEquipamento.ARMA_DIREITA_1,
                        tipos=[TipoArma.ESPADAO]
                    )
                ]
            )
        ],

        TipoClasse.MAGO: [
            ConfiguracaoArma(
                nome="Varinha + Foco",
                armas=[
                    ArmaPermitida(
                        slot=TipoSlotEquipamento.ARMA_DIREITA_1,
                        tipos=[TipoArma.VARINHA]
                    ),
                    ArmaPermitida(
                        slot=TipoSlotEquipamento.ARMA_DIREITA_2,
                        tipos=[TipoArma.FOCO]
                    )
                ]
            ),
            ConfiguracaoArma(
                nome="Cajado",
                armas=[
                    ArmaPermitida(
                        slot=TipoSlotEquipamento.ARMA_DIREITA_1,
                        tipos=[TipoArma.CAJADO]
                    ),
                    ArmaPermitida(
                        slot=TipoSlotEquipamento.ARMA_DIREITA_2,
                        tipos=[TipoArma.CAJADO]
                    )
                ]
            )
        ],

        TipoClasse.LADINO: [
            ConfiguracaoArma(
                nome="Arco/X-Besta + Espada/Adaga + Espada/Adaga",
                armas=[
                    ArmaPermitida(
                        slot=TipoSlotEquipamento.ARMA_ESQUERDA,
                        tipos=[
                            TipoArma.ARCO,
                            TipoArma.XBesta
                        ]
                    ),
                    ArmaPermitida(
                        slot=TipoSlotEquipamento.ARMA_DIREITA_1,
                        tipos=[
                            TipoArma.ESPADA,
                            TipoArma.ADAGA
                        ]
                    ),
                    ArmaPermitida(
                        slot=TipoSlotEquipamento.ARMA_DIREITA_2,
                        tipos=[
                            TipoArma.ESPADA,
                            TipoArma.ADAGA
                        ]
                    )
                ]
            )
        ]
    }

    @staticmethod
    def obter_configuracoes(
        classe: TipoClasse
    ) -> list[ConfiguracaoArma]:

        return EquipamentosSystem.CONFIGURACOES.get(classe, [])

    @staticmethod
    def equipamento_permitido(
        classe: TipoClasse,
        slot: TipoSlotEquipamento,
        tipo_arma: TipoArma
    ) -> bool:

        configuracoes = EquipamentosSystem.obter_configuracoes(
            classe
        )

        for configuracao in configuracoes:
            for arma in configuracao.armas:

                if arma.slot == slot and tipo_arma in arma.tipos:
                    return True

        return False