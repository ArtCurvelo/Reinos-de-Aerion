from app.models.classe import Classe, TipoClasse


class ClasseService:

    @staticmethod
    def obter_classe(tipo: TipoClasse) -> Classe:

        classes = {

            TipoClasse.GUERREIRO: Classe(
                tipo=TipoClasse.GUERREIRO,

                forca=14,
                destreza=9,
                constituicao=14,
                inteligencia=8,
                sabedoria=10,
                carisma=8
            ),

            TipoClasse.MAGO: Classe(
                tipo=TipoClasse.MAGO,

                forca=8,
                destreza=10,
                constituicao=8,
                inteligencia=14,
                sabedoria=12,
                carisma=9
            ),

            TipoClasse.LADINO: Classe(
                tipo=TipoClasse.LADINO,

                forca=10,
                destreza=14,
                constituicao=10,
                inteligencia=10,
                sabedoria=8,
                carisma=12
            )
        }

        return classes[tipo]