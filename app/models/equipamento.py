from enum import Enum

from pydantic import BaseModel, Field


class TipoEquipamento(str, Enum):
    ARMA = "Arma"
    ARMADURA = "Armadura"
    ACESSORIO = "Acessório"


class TipoArma(str, Enum):
    ESPADA = "Espada"
    MACA = "Maça"
    ESPADAO = "Espadão"
    ESCUDO = "Escudo"
    ARCO = "Arco"
    XBesta = "X-Besta"
    ADAGA = "Adaga"
    VARINHA = "Varinha"
    FOCO = "Foco"
    CAJADO = "Cajado"


class Equipamento(BaseModel):
    id: str
    nome: str = Field(min_length=1, max_length=50)
    tipo: TipoEquipamento
    descricao: str = Field(min_length=1, max_length=200)
    valor: int = Field(ge=0)

    tipo_arma: TipoArma | None = None
    maos: int = Field(default=1, ge=1, le=2)

    nivel_requerido: int = Field(default=1, ge=1)

    forca: int = 0
    destreza: int = 0
    constituicao: int = 0
    inteligencia: int = 0
    sabedoria: int = 0
    carisma: int = 0