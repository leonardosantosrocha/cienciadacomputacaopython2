# Criando uma matriz já conhecida
matriz = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(matriz)

# Função para criar matrizes
def cria_matriz(num_linhas, num_colunas):
    ''' (int, int, valor) -> matriz (lista de listas)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas
    colunas em que cada elemento é igual ao valor dado.
    '''
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

# Lendo matriz do teclado
def le_matriz():
    linhas = int(input('Digite o número de linhas da matriz: '))
    colunas = int(input('Digite o número de colunas para da matriz: '))
    matriz = cria_matriz(linhas, colunas)
    print(matriz)

# Executando
le_matriz()