# Importando módulo random
import random

# Crie um programa que recebe um número N e devolve uma lista com N números aleatórios
def lista_grande(n):
    lista = []
    for i in range(n):
        x = random.randint(0, 1000)
        lista.append(x)
    return lista