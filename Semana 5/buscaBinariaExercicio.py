# Eficiência de Busca
#   - Vimos que a Busca Sequencial não é muito eficiente
#   - Que tal levar em conta o fato de que a lista está ordenada?

# Busca Binária
#   - Objetivo: Localizar um elemento X em uma lista
#   - Considere o elemento M do meio da lista
#   - X == M => encontrou o elemento!
#   - X < M => procure apenas na 1° metade (esquerda)
#   - X > M => procure apenas na 2° metade (direita)
#   - Repita o processo até que o X seja encontrado ou que a lista esteja vazia

# Busca Binária
def busca(lista, x):
    # Primeiro elemento da lista
    primeiro = 0
    # Último elemento da lista
    ultimo = len(lista)-1
    # Enquanto primeiro <= último
    while primeiro <= ultimo:
        # Meio da lista é a soma do primeiro e segundo dividido por dois
        meio = (primeiro + ultimo) // 2
        # Se lista[atual] igual x
        if lista[meio] == x:
            print(meio)
            # Retorna lista[atual]
            return meio
        # Se lista[atual] diferente de x
        else:
            # Se x menor que lista[atual]
            if x < lista[meio]:
                # Último = meio - 1
                ultimo = meio - 1
                print(meio)
            # Se x maior que lista[atual]
            else:
                # Primeiro = meio + 1
                primeiro = meio + 1
                print(meio)
    # Caso não encontre
    return False