import uuid
from dataclasses import dataclass, field
from src.domain.enum.veiculo_status import VeiculoStatus

@dataclass
class Veiculo:
    _id: str
    marca: str
    modelo: str
    ano: int
    cor: str
    preco: float = field(default=0.00)
    status: VeiculoStatus = field(default=VeiculoStatus.DISPONIVEL.value,init=True)

    @staticmethod
    def criar(marca: str, modelo: str, ano: int, cor: str, preco: float) -> 'Veiculo':
        return Veiculo(
            _id=str(uuid.uuid4()),
            marca=marca,
            modelo=modelo,
            ano=ano,
            cor=cor,
            preco=preco,
        )

    def atualizar(self, marca: str, modelo: str, ano: int, cor: str, preco: float) -> 'Veiculo':
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.cor=cor
        self.preco=preco
        return self

    @classmethod
    def parseToModel(cls, dataDict):
        return cls(**dataDict)
