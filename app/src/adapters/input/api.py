from fastapi import APIRouter
from src.adapters.input.health_check_router import router as HealthCheck
from src.adapters.input.veiculo_router import router as VeiculoRouter

ROUTER_BASE_URL = "/veiculos"

api_router = APIRouter()
api_router.include_router(HealthCheck, prefix='{}/health'.format(ROUTER_BASE_URL), tags=["healthCheck"])
api_router.include_router(VeiculoRouter, prefix='{}'.format(ROUTER_BASE_URL), tags=["veiculos"])
