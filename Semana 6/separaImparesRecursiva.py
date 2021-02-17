# Crie um programa para separar os números impares de uma lista
def encontra_impares(lista):
    impares = []
    if len(lista) > 0:
        if lista[0] % 2 != 0:
            impares.append(lista[0])
        impares.extend(encontra_impares(lista[1:]))
    return impares

print(encontra_impares([1, 2, 3 ,4 ,5 ,6, 7, 8, 9]))