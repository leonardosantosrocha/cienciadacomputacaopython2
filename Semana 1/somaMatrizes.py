# Crie um programa para realizar a soma entre duas matrizes
def soma_matrizes(m1, m2):
    # Variáveis para comprar dimensão da matriz
    linhas1 = 0
    linhas2 = 0
    colunas1 = len(m1[0])
    colunas2 = len(m2[0])
    # Linhas da primeira matriz
    for i in range(len(m1)):
        linhas1 += 1
    # Linhas da segunda matriz
    for j in range(len(m2)):
        linhas2 += 1
    # Validando as dimensões: diferente, retornar falso
    if linhas1 != linhas2 or colunas1 != colunas2:
        return False
    # Validando as dimensões: iguais, retornar a soma das matrizes
    else:
        # Variável para armazenar a matriz
        matriz = []
        # Laço para percorrer as linhas
        for i in range(len(m1)):
            # Adicionando uma lista vazia a matriz
            matriz.append([])
            # Laço para percorrer as colunas
            for j in range(len(m1[0])):
                # Matriz recebe a soma da linha e coluna das matrizes um e dois
                matriz[i].append(m1[i][j] + m2[i][j])
        # Retornando a matriz
        return matriz

# Execução
# m1 = [[1, 2, 3], [4, 5, 6]]
# m2 = [[2, 3, 4], [5, 6, 7]]
# print(soma_matrizes(m1, m2))