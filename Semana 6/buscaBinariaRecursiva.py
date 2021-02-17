def busca_binaria(lista, elemento, min=0, max=None):
    if max == None:
        max = len(lista) - 1
    
    if max < min:
        return False
    else:
        meio = min + (max-min) // 2
    
    if lista[meio] > elemento:
        return busca_binaria(lista, elemento, min, meio-1)
    
    elif lista[meio] < elemento:
        return busca_binaria(lista, elemento, meio+1, max)

    else:
        return meio


print(busca_binaria([1, 2, 3, 4, 5], 4, ))