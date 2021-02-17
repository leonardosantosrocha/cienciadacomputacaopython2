# Crie uma classe para mostrar os lados e perimetro de um triangulo
class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        p = self.a + self.b + self.c
        return p