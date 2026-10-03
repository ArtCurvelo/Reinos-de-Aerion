from app.models.classe import TipoClasse
from app.models.jogador import Jogador
from app.services.classe_service import ClasseService


class PersonagemService:

    @staticmethod
    def criar_jogador(nome: str, tipo_classe: TipoClasse) -> Jogador:

        dados_classe = ClasseService.obter_classe(tipo_classe)

        jogador = Jogador(
            nome=nome,
            classe=tipo_classe,

            vida=dados_classe.vida_base,
            vida_maxima=dados_classe.vida_base,

            mana=dados_classe.mana_base,
            mana_maxima=dados_classe.mana_base,

            forca=dados_classe.forca,
            inteligencia=dados_classe.inteligencia,
            destreza=dados_classe.destreza
        )

        return jogador