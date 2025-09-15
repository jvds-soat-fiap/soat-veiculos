import unittest
from unittest.mock import MagicMock
from src.application.usecase.atualizar_veiculo_usecase import AtualizarVeiculoUseCase
from src.domain.veiculo import Veiculo
from src.domain.enum.veiculo_status import VeiculoStatus

class TestAtualizarVeiculoUseCase(unittest.TestCase):

    def setUp(self):
        self.mock_repo = MagicMock()
        self.usecase = AtualizarVeiculoUseCase(repositorio=self.mock_repo)

        self.veiculo_original = MagicMock(spec=Veiculo)
        self.mock_repo.findById.return_value = self.veiculo_original

        self.veiculo_update = MagicMock(spec=Veiculo)
        self.veiculo_update.marca = "Ford"
        self.veiculo_update.modelo = "Fiesta"
        self.veiculo_update.ano = 2020
        self.veiculo_update.cor = "Azul"
        self.veiculo_update.preco = 45000.0

    def test_update_deve_atualizar_veiculo_e_salvar(self):
        resultado = self.usecase.update("123", self.veiculo_update)

        self.mock_repo.findById.assert_called_once_with("123")
        self.veiculo_original.atualizar.assert_called_once_with(
            marca="Ford",
            modelo="Fiesta",
            ano=2020,
            cor="Azul",
            preco=45000.0
        )
        self.mock_repo.update.assert_called_once_with(self.veiculo_original)
        self.assertEqual(resultado, self.veiculo_original)

    def test_status_deve_atualizar_status_e_salvar(self):
        resultado = self.usecase.status("123", VeiculoStatus.VENDIDO)

        self.mock_repo.findById.assert_called_once_with("123")
        self.assertEqual(self.veiculo_original.status, VeiculoStatus.VENDIDO.value)
        self.mock_repo.update.assert_called_once_with(self.veiculo_original)
        self.assertEqual(resultado, self.veiculo_original)

if __name__ == "__main__":
    unittest.main()
