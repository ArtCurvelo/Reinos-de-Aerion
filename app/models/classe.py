from enum import Enum

from pydantic import BaseModel


class TipoClasse(str, Enum):
    GUERREIRO = "Guerreiro"
    MAGO = "Mago"
    LADINO = "Ladino"


class Classe(BaseModel):
    tipo: TipoClasse

    vida_base: int
    mana_base: int

    forca: int
    inteligencia: int
    destreza: int