# Crie um programa para imprimir matrizes linha a linha
def imprime_matriz(minha_matriz):
    for i in range(len(minha_matriz)):
        elemento = str(minha_matriz[i])
        x = elemento.replace('[','').replace(']','').replace(',','')
        print(x)

# Execução
# minha_matriz = [[1, 2, 3], [4, 5, 6]]
# imprime_matriz(minha_matriz)