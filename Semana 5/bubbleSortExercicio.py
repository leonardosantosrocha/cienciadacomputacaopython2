# Bubble Sort
def bubble_sort(lista):
    fim = len(lista)
    # Começando no fim da lista, até a posição zero, decrementando
    for i in range(fim-1, 0, -1):
        # Começando no inicio da lista
        for j in range(i):
            # Se o elemento atual 'j' for maior que o próximo 'j+1'
            if lista[j] > lista[j+1]:
                # O elemento atual será o próximo
                lista[j], lista[j+1] = lista[j+1], lista[j]
                print(lista)
    return lista