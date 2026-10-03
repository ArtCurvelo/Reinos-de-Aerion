from pydantic import BaseModel, Field
from app.models.classe import TipoClasse

class Jogador(BaseModel):
    nome: str = Field(min_length=3, max_length=30)
    classe: TipoClasse

    nivel: int = 1
    experiencia: int = 0
    ouro: int = 100

    vida: int
    vida_maxima: int

    mana: int
    mana_maxima: int

    forca: int
    inteligencia: int
    destreza: int