from src.adapters.input.schema.veiculo_request import VeiculoRequest
from src.domain.veiculo import Veiculo


class VeiculoMapper:
    @staticmethod
    def parseToDomain(request: VeiculoRequest) -> Veiculo:
        return Veiculo(    
            _id=None,        
            marca=request.marca,
            modelo=request.modelo,
            ano=request.ano,
            cor=request.cor,
            preco=request.preco
        )

    # @staticmethod
    # def parseToResponseList(domainList: List[Order]) -> BaseResponse[OrderResponse]:
    #     return BaseResponse(
    #         data=[OrderMapper.parseToResponse(domain).data for domain in domainList]
    #     )        
