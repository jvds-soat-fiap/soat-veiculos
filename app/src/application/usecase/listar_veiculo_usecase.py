from typing import List
from src.adapters.output.repository.repository import Repository
from src.domain.veiculo import Veiculo
from src.domain.enum.veiculo_status import VeiculoStatus

class ListarVeiculoUseCase:
    def __init__(self, repositorio: Repository):
        self._repositorio = repositorio

    def executar(self, status: VeiculoStatus) -> List[Veiculo]:
        veiculoList = self._repositorio.findByFilter(filter={'status': status.value})
        veiculoList.sort(key=lambda veiculo: veiculo['preco'], reverse=False)        
        return veiculoList
