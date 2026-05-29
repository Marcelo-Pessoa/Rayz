import unittest
from main import RaizQuad, Potencia

class TestCalculos(unittest.TestCase):

    # [CT01] Calcular Raiz Quadrada Válida
    def test_ct01_raiz_valida(self):
        self.assertEqual(RaizQuad(9), 3)

    # [CT02] Raiz Quadrada Entrada Inválida Negativa
    def test_ct02_raiz_invalida_negativa(self):
        self.assertEqual(RaizQuad(-4), -1)
        
    # [CT03] Calcular Raiz Quadrada Inválida Número Ponto Flutuante
    def test_ct03_raiz_invalida_ponto_flutuante(self):
        self.assertEqual(RaizQuad(2.63), )

    # [CT04] Raiz Quadrada Inválida Não-Número
    def test_ct04_raiz_invalida_nao_numero(self):
        self.assertEqual(RaizQuad("texto"), -1)

    # [CT05] Calcular Potência Válida
    def test_ct05_potencia_valida(self):
        self.assertEqual(Potencia(2, 3), 8)

    # [CT05] Calcular Potência Válida de Base Negativa
    def test_ct05_2_potencia_invalida_negativa(self):
        self.assertEqual(Potencia(-2, 3), -8)

    # [CT06] Potência Entrada de Expoente Negativo
    def test_ct06_potencia_invalida_negativa(self):
        self.assertEqual(Potencia(2, -3), -1)

    # [CT07] Potência Inválida Número Ponto Flutuante
    def test_ct07_potencia_invalida_ponto_flutuante(self):
        self.assertEqual(Potencia(2.63, 3), -1)

    # [CT08] Potência Inválida Não-Número
    def test_ct08_potencia_invalida_nao_numero(self):
        self.assertEqual(Potencia("texto", 3), -1)

if __name__ == '__main__':
    unittest.main()