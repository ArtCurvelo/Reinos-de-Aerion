from app.models.classe import TipoClasse
from app.models.jogador import Jogador
from app.services.classe_service import ClasseService
from app.systems.atributos import AtributosSystem


class PersonagemService:

    @staticmethod
    def criar_jogador(
        nome: str,
        tipo_classe: TipoClasse
    ) -> Jogador:

        dados_classe = ClasseService.obter_classe(tipo_classe)

        jogador = Jogador(
            nome=nome,
            classe=tipo_classe,

            forca=dados_classe.forca,
            destreza=dados_classe.destreza,
            constituicao=dados_classe.constituicao,
            inteligencia=dados_classe.inteligencia,
            sabedoria=dados_classe.sabedoria,
            carisma=dados_classe.carisma
        )

        return jogador

    @staticmethod
    def aumentar_atributo(
        jogador: Jogador,
        atributo: str
    ) -> Jogador:

        atributos_validos = {
            "forca",
            "destreza",
            "constituicao",
            "inteligencia",
            "sabedoria",
            "carisma"
        }

        if atributo not in atributos_validos:
            raise ValueError("Atributo inválido.")

        valor_atual = getattr(jogador, atributo)

        novo_valor, pontos_restantes = AtributosSystem.aumentar(
            valor_atual,
            jogador.pontos_atributo
        )

        setattr(jogador, atributo, novo_valor)
        jogador.pontos_atributo = pontos_restantes

        return jogador

    @staticmethod
    def diminuir_atributo(
        jogador: Jogador,
        atributo: str
    ) -> Jogador:

        atributos_validos = {
            "forca",
            "destreza",
            "constituicao",
            "inteligencia",
            "sabedoria",
            "carisma"
        }

        if atributo not in atributos_validos:
            raise ValueError("Atributo inválido.")

        valor_atual = getattr(jogador, atributo)

        novo_valor, pontos_devolvidos = (
            AtributosSystem.diminuir(valor_atual)
        )

        setattr(jogador, atributo, novo_valor)

        jogador.pontos_atributo += pontos_devolvidos

        return jogador