import unittest
from calculadora import Calculadora
 
class teste_classe_calculadora(unittest.TestCase):
 
    def test_adicao(self):
        calc = Calculadora()
        result = calc.adicao(2,2)
        self.assertEqual(4, result)

    def test_subtratacao(self):
        calc = Calculadora()
        result = calc.subtracao(2,2)
        self.assertEqual(0, result)

    def test_multiplicacao(self):
        calc = Calculadora()
        result = calc.multiplicacao(2,3)
        self.assertEqual(6, result)

    def test_divisao(self):
        calc = Calculadora()
        result = calc.divisao(8,2)
        self.assertEqual(4, result)

    def test_potencia(self):
        calc = Calculadora()
        result = calc.potencia(2,4)
        self.assertEqual(16, result)

    def test_raiz(self):
        calc = Calculadora()
        result = calc.raiz(25)
        self.assertEqual(5, result)

    def test_log10(self):
        calc = Calculadora()
        result = calc.log10(10)
        self.assertEqual(1, result)


if __name__ == '__main__':
    unittest.main()
