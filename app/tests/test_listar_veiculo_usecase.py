import unittest
from unittest.mock import MagicMock
from src.application.usecase.listar_veiculo_usecase import ListarVeiculoUseCase
from src.domain.enum.veiculo_status import VeiculoStatus

class TestListarVeiculoUseCase(unittest.TestCase):
    def setUp(self):
        self.mock_repositorio = MagicMock()
        self.usecase = ListarVeiculoUseCase(repositorio=self.mock_repositorio)

    def test_executar_deve_retornar_veiculos_ordenados_por_preco(self):
        # mock
        status = VeiculoStatus.DISPONIVEL
        veiculos_mock = [
            {'id': 1, 'preco': 50000},
            {'id': 2, 'preco': 30000},
            {'id': 3, 'preco': 40000}
        ]
        self.mock_repositorio.findByFilter.return_value = veiculos_mock

        # usecase
        resultado = self.usecase.executar(status)

        # validacao
        self.mock_repositorio.findByFilter.assert_called_once_with(filter={'status': status.value})
        precos = [veiculo['preco'] for veiculo in resultado]
        self.assertEqual(precos, [30000, 40000, 50000])

if __name__ == '__main__':
    unittest.main()
