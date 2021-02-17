# Bubble Sort Melhorado
#   - Percorre a lista múltiplas vezes; a cada passagem, compara todos
# os elementos adjacentes e troca de lugar os que estiverem fora de ordem.
#   - Melhoria: se em uma das interações, nenhuma troca é realizada, isso
# significa que a lista já está ordenada e podemos finalizar o algoritmo.

# Bubble Sort Melhorado
def bubbleSortPlus(lista):
    fim = len(lista)
    # Começando no fim da lista, até a posição zero, decrementando
    for i in range(fim-1, 0, -1):
        # Variável de troca
        trocou = False
        # Começando no inicio da lista
        for j in range(i):
            # Se o elemento atual 'j' for maior que o próximo 'j+1'
            if lista[j] > lista[j+1]:
                # O elemento atual será o próximo
                lista[j], lista[j+1] = lista[j+1], lista[j]
                # Se executou uma troca
                trocou = True
        # Condição de parada
        if trocou == False:
            return lista