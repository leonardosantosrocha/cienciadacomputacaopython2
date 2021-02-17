# Bubble Sort
#   - Pense em uma lista como um tubo de ensaio vertical onde os elementos mais 
# leves sobem à superficie como uma bolha e os mais pesados afundam.
#   - Percorre a lista múltiplas vezes; a cada passagem, compara todos os elementos
# adjacentes e troca de lugar os que estiverem fora de ordem.
#   - A cada passagem, o elemento mais pesado se deposita no fundo do tubo de
# ensaio,o maior elemento da lista vai para o final dela.

# Bubble Sort
def bubbleSort(lista):
    fim = len(lista)
    # Começando no fim da lista, até a posição zero, decrementando
    for i in range(fim-1, 0, -1):
        # Começando no inicio da lista
        for j in range(i):
            # Se o elemento atual 'j' for maior que o próximo 'j+1'
            if lista[j] > lista[j+1]:
                # O elemento atual será o próximo
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista