# Crie uma classe para mostrar os lados e perimetro de um triangulo
class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tipo_lado(self):
        # Escaleno
        if self.a != self.b and self.a != self.c and self.b != self.c:
            return 'escaleno'
        # Equilátero
        elif self.a == self.b and self.a == self.c and self.b == self.c:
            return 'equilátero'
        else:
            return 'isósceles'

t = Triangulo(3, 4, 5)
print(t.tipo_lado())