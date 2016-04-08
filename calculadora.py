import math

class Calculadora(object):
 
    def adicao(self, x, y):
        return x+y

    def subtracao(self, x, y):
        return x-y

    def multiplicacao(self, x, y):
        return x*y

    def divisao(self, x, y):
        return x/y

    def potencia(self, x, y):
        return math.pow(x,y)