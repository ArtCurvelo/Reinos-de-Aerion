from enum import Enum

from pydantic import BaseModel, Field


class TipoItem(str, Enum):
    ARMA = "Arma"
    ARMADURA = "Armadura"
    ACESSORIO = "Acessório"
    CONSUMIVEL = "Consumível"
    MATERIAL = "Material"
    QUEST = "Quest"


class Item(BaseModel):
    id: str
    nome: str = Field(min_length=1, max_length=50)
    tipo: TipoItem

    descricao: str = Field(
        min_length=1,
        max_length=200
    )

    valor: int = Field(ge=0)
    quantidade: int = Field(ge=1)