import unittest
from prefect.testing.utilities import prefect_test_harness  #indicação e fornecimento de suporte para executar é um arquivo com conjunto de testes, coletar resultados e verificar se a saída ta correta

from flows.flow_versao1 import somar, subtrair

class TestTarefasCalculadora(unittest.TestCase):

    def test_01_somar(self):   #ao começar com test_, o unittest vai identificar automaticamente
        with prefect_test_harness():
            resultado = somar.fn(10, 5)  #fn chama a função decorada com @task, sem executar o runtime do prefect, facilitando os testes.
            self.assertEqual(resultado, 15) #verifica se retorna corretamente

    def test_02_subtrair(self):
        with prefect_test_harness():
            resultado = subtrair.fn(10, 5)
            self.assertEqual(resultado, 5)

    def test_03_somar_negativos(self):
        with prefect_test_harness():
            resultado = somar.fn(-10, -5)
            self.assertEqual(resultado, -15)

    def test_04_subtrair_negativos(self):
        with prefect_test_harness():
            resultado = subtrair.fn(-10, -5)
            self.assertEqual(resultado, -5)

    def test_05_somar_zero(self):
        with prefect_test_harness():
            resultado = somar.fn(0, 0)
            self.assertEqual(resultado, 0)

    def test_06_subtrair_zero(self):
        with prefect_test_harness():
            resultado = subtrair.fn(0, 0)
            self.assertEqual(resultado, 0)

if __name__ == '__main__':
    unittest.main()

