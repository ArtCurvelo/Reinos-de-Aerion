from enum import Enum

from pydantic import BaseModel


class TipoClasse(str, Enum):
    GUERREIRO = "Guerreiro"
    MAGO = "Mago"
    LADINO = "Ladino"


class Classe(BaseModel):
    tipo: TipoClasse

    forca: int
    destreza: int
    constituicao: int
    inteligencia: int
    sabedoria: int
    carisma: int