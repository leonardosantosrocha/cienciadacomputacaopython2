# Algoritmos de ordenação

# Seleção Direta (Selection Sort)
#   - 1° passo: busca o 1° elemento de todos e coloca na posição inicial da lista;
#   - 2° passo: busca o 2° menor elemento da lista e o coloca na 2° posição da lsita;
#   - 3° passo: busca o 3° menor elemento da lista e o coloca na 3° posição da lsita;
#   - Finalizar: repetir até a lista estar ordenada.

class Ordenador:
    def selecao_direta(self, lista):
        fim = len(lista)

        for i in range(fim - 1):
            posicao_do_minimo = i

            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j
        lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]