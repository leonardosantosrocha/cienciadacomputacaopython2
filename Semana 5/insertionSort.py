# Crie o algoritmo 
import random
    
def insertion_sort(lista):
    for k in range(1,len(lista)):
        x = lista[k]
        i = k
        while i > 0 and x < lista[i-1]:
            lista[i] = lista[i-1]
            i = i - 1
        lista[i] = x
    return lista