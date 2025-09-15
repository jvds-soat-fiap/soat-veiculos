import unittest
from unittest.mock import MagicMock, patch
from src.application.usecase.cadastrar_veiculo_usecase import CadastrarVeiculoUseCase
from src.domain.veiculo import Veiculo

class TestCadastrarVeiculoUseCase(unittest.TestCase):
    @patch('src.adapters.output.repository.repository.Repository')
    @patch('src.domain.veiculo.Veiculo.criar')
    def test_executar_deve_criar_e_salvar_veiculo(self, mock_criar, mock_repository_class):
        mock_repository = MagicMock()
        mock_repository_class.return_value = mock_repository

        veiculo_mock = MagicMock(spec=Veiculo)
        mock_criar.return_value = veiculo_mock

        use_case = CadastrarVeiculoUseCase(mock_repository)

        marca = "Toyota"
        modelo = "Corolla"
        ano = 2022
        cor = "Prata"
        preco = 85000.0

        # usecase
        resultado = use_case.executar(marca, modelo, ano, cor, preco)

        # validacao
        mock_criar.assert_called_once_with(marca, modelo, ano, cor, preco)
        mock_repository.save.assert_called_once_with(veiculo_mock)
        self.assertEqual(resultado, veiculo_mock)

if __name__ == '__main__':
    unittest.main()
