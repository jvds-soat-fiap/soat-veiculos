import unittest
from unittest.mock import MagicMock
from src.adapters.output.repository.repository import Repository
from src.application.usecase.editar_veiculo_usecase import EditarVeiculoUseCase

class TestEditarVeiculoUseCase(unittest.TestCase):
    def setUp(self):
        # mock
        self.mock_repositorio = MagicMock(spec=Repository)
        self.use_case = EditarVeiculoUseCase(repositorio=self.mock_repositorio)

    def test_executar_deve_retornar_veiculo(self):
        # mock
        veiculo_id = 123
        veiculo_esperado = {"id": veiculo_id, "modelo": "Maverick"}
        self.mock_repositorio.findById.return_value = veiculo_esperado

        # usecase
        resultado = self.use_case.executar(veiculo_id)

        # resultado
        self.assertEqual(123, resultado["id"])