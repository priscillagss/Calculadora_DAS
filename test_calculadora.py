import unittest
 
class teste_classe_calculadora(unittest.TestCase):
 
    def test_adicao(self):
        calc = Calculator()
        result = calc.adicao(2,2)
        self.assertEqual(4, result)
