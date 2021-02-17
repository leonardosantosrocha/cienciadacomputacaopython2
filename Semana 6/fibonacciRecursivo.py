# Crie um programa para calcular a sequência de fibonacci de forma recursiva
def fibonacci(n):
    if n <= 1: # Base da recursão
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) # Chamada recursiva