from enum import Enum


class TipoSlotEquipamento(str, Enum):
    CABECA = "Cabeça"
    PEITORAL = "Peitoral"
    LUVAS = "Luvas"
    CALCAS = "Calças"
    BOTAS = "Botas"

    ARMA_ESQUERDA = "Arma Esquerda"
    ARMA_DIREITA_1 = "Arma Direita 1"
    ARMA_DIREITA_2 = "Arma Direita 2"

    ACESSORIO_1 = "Acessório 1"
    ACESSORIO_2 = "Acessório 2"
    ACESSORIO_3 = "Acessório 3"