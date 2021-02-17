# Crie um programa para multiplicar matrizes
def cria_matriz(num_linhas, num_colunas):
    matriz = [] # Lista vazia
    for i in range(num_linhas):
        # Cria a linha i
        linha = [] # Lista vazia
        for j in range(num_colunas):
            # Adicionando colunas
            valor = int(input('Digite o elemento [' + str(i) + '][' + str(j) + ']: ')) 
            linha.append(valor)
            # Adicionando linha a matriz
        matriz.append(linha)
    return matriz

def multiplica_matrizes(a, b):
    # Variáveis de apoio para produto entre matrizes
    linhas_a, colunas_a = len(a), len(a[0])
    linhas_b, colunas_b = len(b), len(b[0])
    # Verificando se podemos realizar o produto entre as matrizes
    if colunas_a == linhas_b:
        # Criando a matriz
        matriz = []
        # Criando o laço para adicionar linhas
        for linha in range(linhas_a):
            # Adicionando linhas na matriz
            matriz.append([])
            # Criando um laço para adicionar colunas
            for coluna in range(colunas_b):
                # Adicionando as colunas
                matriz[linha].append(0)
                # Criando um laço para adicionar elementos
                for k in range(colunas_a):
                    # Adicionando elementos
                    matriz[linha][coluna] += a[linha][k] * b[k][coluna]
        # Retornando a matriz
        return matriz
    # Retornando falso caso não seja possui produzir o produto da matriz
    else:
        return False

def main():
    # Criando matrizes
    matriz1 = cria_matriz(2, 2)
    matriz2 = cria_matriz(2, 2)
    print()
    # Imprimindo matrizes
    for i in range(len(matriz1)):
        print(matriz1[i])
    print()
    for i in range(len(matriz2)):
        print(matriz2[i])
    print()
    # Multiplicação de matrizes
    produto = multiplica_matrizes(matriz1, matriz2)
    # Imprimindo o produto da matriz
    for i in range(len(produto)):
        print(produto[i])
main()