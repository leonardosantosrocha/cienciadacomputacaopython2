# Crie um programa para mostrar as dimensões de uma matriz
def dimensoes(matriz):
    # Percorrendo a quantidade de linhas
    linhas = 0
    for i in range(len(matriz)):
        linhas += 1
    # Setando a quantidade de colunas
    colunas = len(matriz[0])
    # Retornando o valor iXj (linhas X colunas)
    return f'{str(linhas)}X{str(colunas)}'

# Execução
# minha_matriz = [[1], [2]]
# dimensoes(minha_matriz)