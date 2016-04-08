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

if __name__ == '__main__':
    unittest.main()
