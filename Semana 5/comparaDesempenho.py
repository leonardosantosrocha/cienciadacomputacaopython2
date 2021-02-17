# Comparação de Desempenho
#   - Módulo time
#       - Função time()
#       - Devolve o tempo decorrido (em segundos) desde 01/01/1970

# Importando o módulo 'time'
import time, random

# Antes da execução do código
antes = time.time()

# Criando o programa a ser cronometrado
def lista_aleatoria(n):
    lista = []
    for i in range(n):
        lista.append(random.randint(0, 1000))
    return lista
# Executando o programa a ser cronometrado
lista_aleatoria(5000000)

# Depois da execução do código
depois = time.time()

# Calculando o tempo de execução
print(f'O tempo gasto foi', depois - antes)