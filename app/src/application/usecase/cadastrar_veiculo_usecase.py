from src.adapters.output.repository.repository import Repository
from src.domain.veiculo import Veiculo

class CadastrarVeiculoUseCase:
    def __init__(self, repositorio: Repository):
        self.repositorio = repositorio

    def executar(self, marca, modelo, ano, cor, preco):
        veiculo = Veiculo.criar(marca, modelo, ano, cor, preco)
        self.repositorio.save(veiculo)
        return veiculo
