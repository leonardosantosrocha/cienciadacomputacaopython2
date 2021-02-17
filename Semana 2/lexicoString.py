# Crie um programa para mostrar a menor string na ordem lexicográfica
def primeiro_lex(lista):
    string = '~'
    for i in range(len(lista)):
        if ord(lista[i][0]) < ord(string[0][0]):
            string = lista[i]
    return string