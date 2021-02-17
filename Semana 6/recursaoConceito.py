# Recursão
#   - Muitos problemas contém, dentro de si, problemas menores
#       - Que são similares ao problema maior
#   - Esses problemas tem uma estrutura recursiva
#   - Podemos aplicar uma solução recursiva

# Como resolver um problema recursivo: um algoritmo recursivo
#   - Se o tamanho do problema for pequeno
#       - Resolva-o diretamente
#   - Se não for
#       - Reduza-o a uma instância menor do mesmo problemas
#       - Aplique o algoritmo recursivamente a instância menor
#       - Volte a instância original e tente resolver

# Exemplos de algoritmos recursivos
#   - Fatorial
#   - Fibonacci
#   - Busca Binária
#   - MergeSort

# Fatorial Recursivo
def fatorial(n):
    if n <= 1: # Base da recursão
        return 1
    else:
        return n * fatorial(n-1) # Chamada recursiva

# Fibonacci Recursivo
def fibonacci(n):
    if n <= 1: # Base da recursão
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) # Chamada recursiva