from src.adapters.output.repository.repository import Repository
from src.domain.veiculo import Veiculo
from src.domain.enum.veiculo_status import VeiculoStatus

class AtualizarVeiculoUseCase:
    def __init__(self, repositorio: Repository):
        self.repositorio = repositorio

    def update(self, veiculo_id: str, veiculo_update: Veiculo):
        veiculo : Veiculo = self.repositorio.findById(veiculo_id)
        veiculo.atualizar(
            marca=veiculo_update.marca,
            modelo=veiculo_update.modelo,
            ano=veiculo_update.ano,
            cor=veiculo_update.cor,
            preco=veiculo_update.preco
        )
        self.repositorio.update(veiculo)
        return veiculo

    def status(self, veiculo_id, status: VeiculoStatus):
        veiculo : Veiculo = self.repositorio.findById(veiculo_id)
        veiculo.status = status.value 
        self.repositorio.update(veiculo)
        return veiculo
