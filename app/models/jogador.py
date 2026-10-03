from pydantic import BaseModel, Field

from app.models.classe import TipoClasse


class Jogador(BaseModel):
    nome: str = Field(min_length=3, max_length=30)
    classe: TipoClasse

    nivel: int = 1
    experiencia: int = 0
    experiencia_maxima: int = 100
    ouro: int = 100
    pontos_habilidade: int = 0

    forca: int = Field(ge=8, le=20)
    destreza: int = Field(ge=8, le=20)
    constituicao: int = Field(ge=8, le=20)
    inteligencia: int = Field(ge=8, le=20)
    sabedoria: int = Field(ge=8, le=20)
    carisma: int = Field(ge=8, le=20)

    pontos_atributo: int = 3