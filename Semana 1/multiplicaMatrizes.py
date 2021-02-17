# Crie um programa que diz se as matrizes são multiplicaveis ou não
def sao_multiplicaveis(m1, m2):
    linhas = len(m2)
    colunas = len(m1[0])
    if linhas == colunas:
        return True
    else:
        return False

# Execução
# m1 = [[1], [2], [3]]
# m2 = [[1, 2, 3]]
# sao_multiplicaveis(m1, m2)