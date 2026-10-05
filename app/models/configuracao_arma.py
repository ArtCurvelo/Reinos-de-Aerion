from pydantic import BaseModel, Field

from app.models.equipamento import TipoArma
from app.models.slot_equipamento import TipoSlotEquipamento


class ArmaPermitida(BaseModel):
    slot: TipoSlotEquipamento
    tipos: list[TipoArma] = Field(min_length=1)


class ConfiguracaoArma(BaseModel):
    nome: str = Field(min_length=1, max_length=50)
    armas: list[ArmaPermitida] = Field(min_length=1)