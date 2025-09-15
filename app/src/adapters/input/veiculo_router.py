from fastapi import APIRouter, status, Path
from pydantic import BaseModel
from typing import Optional
from src.adapters.output.repository.veiculo_repository import VeiculoRepository
from src.application.usecase.cadastrar_veiculo_usecase import CadastrarVeiculoUseCase
from src.application.usecase.editar_veiculo_usecase import EditarVeiculoUseCase
from src.application.usecase.atualizar_veiculo_usecase import AtualizarVeiculoUseCase
from src.application.usecase.listar_veiculo_usecase import ListarVeiculoUseCase
from src.domain.enum.veiculo_status import VeiculoStatus
from src.adapters.input.schema.veiculo_request import VeiculoRequest
from src.adapters.input.mapper.veiculo_mapper import VeiculoMapper


_repositorio = VeiculoRepository()
_cadastrar_use_case = CadastrarVeiculoUseCase(_repositorio)
_atualizar_use_case = AtualizarVeiculoUseCase(_repositorio)
_listar_use_case = ListarVeiculoUseCase(_repositorio)
_editar_use_case = EditarVeiculoUseCase(_repositorio)


class VeiculoInput(BaseModel):
    marca: str
    modelo: str
    ano: int
    cor: str
    preco: float

class EditarVeiculoInput(BaseModel):
    marca: Optional[str] = None
    modelo: Optional[str] = None
    ano: Optional[int] = None
    cor: Optional[str] = None
    preco: Optional[float] = None


router = APIRouter()

@router.post(path='/', status_code=status.HTTP_201_CREATED)
def cadastrar_veiculo(input: VeiculoInput):
    veiculo = _cadastrar_use_case.executar(
        input.marca, input.modelo, input.ano, input.cor, input.preco
    )
    return veiculo

@router.put(path='/{veiculo_id}', status_code=status.HTTP_200_OK)
def atualizar_veiculo(veiculo_id :str,request: VeiculoRequest):
    veiculo = _atualizar_use_case.update(veiculo_id,VeiculoMapper.parseToDomain(request))
    return veiculo

@router.get(path='/disponivel', status_code=status.HTTP_200_OK)
def listar_disponiveis():
    return _listar_use_case.executar(status=VeiculoStatus.DISPONIVEL)

@router.get(path='/vendidos', status_code=status.HTTP_200_OK)
def listar_vendidos():
    return _listar_use_case.executar(status=VeiculoStatus.VENDIDO)

@router.get(path='/{veiculo_id}', status_code=status.HTTP_200_OK)
def editar_veiculo(veiculo_id: str):
    veiculo = _editar_use_case.executar(veiculo_id)
    return veiculo

@router.patch(path='/{veiculo_id}/reservar', status_code=status.HTTP_204_NO_CONTENT)
def alterar_status_reservar(veiculo_id: str):
    veiculo = _atualizar_use_case.status(veiculo_id=veiculo_id, status=VeiculoStatus.RESERVADO)
    return veiculo

@router.patch(path='/{veiculo_id}/cancelar/reserva', status_code=status.HTTP_204_NO_CONTENT)
def alterar_status_cancelar(veiculo_id: str):
    veiculo = _atualizar_use_case.status(veiculo_id=veiculo_id, status=VeiculoStatus.DISPONIVEL)
    return veiculo

@router.patch(path='/{veiculo_id}/vendido', status_code=status.HTTP_204_NO_CONTENT)
def atualizar_status_vendido(veiculo_id: str):
    veiculo = _atualizar_use_case.status(veiculo_id=veiculo_id,status=VeiculoStatus.VENDIDO)
    return veiculo
