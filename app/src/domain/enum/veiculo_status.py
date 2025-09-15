from enum import Enum

class VeiculoStatus(Enum):
    DISPONIVEL = "DISPONIVEL"
    RESERVADO = "RESERVADO"
    VENDIDO = "VENDIDO"
    PAGO = "PAGO"

    @classmethod
    def valueOfValid(cls, value) -> bool:
        return any(enumType for enumType in cls if enumType.value == str(value).upper() or enumType.name == str(value).upper())

    @classmethod
    def valueOf(cls, value):
        for enumType in cls:
            if (enumType.value == str(value).upper() or enumType.name == str(value).upper()):
                return enumType
        return None
