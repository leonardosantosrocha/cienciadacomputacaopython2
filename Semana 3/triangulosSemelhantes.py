# Crie uma classe para mostrar os lados e perimetro de um triangulo
class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def semelhantes(self, triangulo):
        t2 = triangulo
        lista_t1 = [self.a, self.b, self.c]
        lista_t2 = [t2.a, t2.b, t2.c]

        lista_t1.sort()
        lista_t2.sort()

        if lista_t1[0] / lista_t2[0] == lista_t1[1] / lista_t2[1] == lista_t1[2] / lista_t2[2]:
            return True
        else:
            return False