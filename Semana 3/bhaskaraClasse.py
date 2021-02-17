# Crie um programa para realizar o bhaskara
import math

# Criando a classe 'Bhaskara's
class Bhaskara:
    # Criando o objeto delta 'self' como método construtor
    def delta(self, a, b, c):
        # Retornando o resultado
        return b ** 2 - 4 * a * c

    # Criando o objeto main 'self' como método construtor
    def main(self):
        # Valores de entrada da equação de segundo grau 'a', 'b' e 'c'
        a_digitado = float(input('Digite o valor de a: '))
        b_digitado = float(input('Digite o valor de b: '))
        c_digitado = float(input('Digite o valor de c: '))
        # Mostrando o valor
        print(self.calcula_raizes(a_digitado, b_digitado, c_digitado))

    # Criando o objeto calcula_raizes 'self' como método construtor
    def calcula_raizes(self, a, b, c):
        # Armazenando o resultado de delta
        d = self.delta(a, b, c)
        # Condição se delta igual a zero
        if d == 0:
            # Somente uma raiz é calculada
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            # Retornando o número de raizes e a raiz
            return 1, raiz1
        # Condição se delta diferente de zero
        else:
            # Se delta é menor que zero
            if d < 0:
                # Retornando o número de raizes e a raiz
                return 0
            # Se delta é maior que zero
            else:
                # Retornando o número de raizes e a raiz
                raiz1 = (-b + math.sqrt(d)) / (2* a)
                raiz2 = (-b - math.sqrt(d)) / (2* a)
                return 2, raiz1, raiz2