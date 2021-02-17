# Crie um programa para calcular o fatorial recursivamente
def fatorial(x):
    if x <= 1: # Base da recursão
        return 1
    else:
        return x * fatorial(x-1) # Chamada recursiva