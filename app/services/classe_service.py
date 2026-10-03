from app.models.classe import Classe, TipoClasse


class ClasseService:

    @staticmethod
    def obter_classe(tipo: TipoClasse) -> Classe:

        classes = {
            TipoClasse.GUERREIRO: Classe(
                tipo=TipoClasse.GUERREIRO,
                vida_base=100,
                mana_base=35,
                forca=13,
                inteligencia=5,
                destreza=8
            ),

            TipoClasse.MAGO: Classe(
                tipo=TipoClasse.MAGO,
                vida_base=50,
                mana_base=120,
                forca=4,
                inteligencia=14,
                destreza=8
            ),

            TipoClasse.LADINO: Classe(
                tipo=TipoClasse.LADINO,
                vida_base=70,
                mana_base=50,
                forca=9,
                inteligencia=7,
                destreza=12
            )
        }

        return classes[tipo]