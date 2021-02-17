# Crie um algoritmo para mostrar a posição de um número na lista, caso contrário retorne falso
def busca(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False