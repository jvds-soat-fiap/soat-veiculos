from src.adapters.output.repository.repository_default import RepositoryDefault
from src.domain.veiculo import Veiculo

class VeiculoRepository(RepositoryDefault[Veiculo, str]):
    def __init__(self) -> None:
        super().__init__(Veiculo)


    def parseToModel(self, dict):
        return Veiculo.parseToModel(dict)
