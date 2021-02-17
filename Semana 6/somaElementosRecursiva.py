# Crie um programa para somar elementos de uma lista de forma recursiva
def soma_lista(lista):
    if len(lista) <= 1:
        return lista[0]
    else:
        return lista[0] + soma_lista(lista[1:])

print(soma_lista([1, 2, 3, 4, 5, 6]))