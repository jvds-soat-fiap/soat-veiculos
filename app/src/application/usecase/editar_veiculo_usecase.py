from src.adapters.output.repository.repository import Repository

class EditarVeiculoUseCase:
    def __init__(self, repositorio: Repository):
        self.repositorio = repositorio

    def executar(self, veiculo_id):
        veiculo = self.repositorio.findById(veiculo_id)
        return veiculo
