# Crie um programa que concatena as letras maiúsculas de uma frase
def maiusculas(frase):
    string = ''
    for i in range(len(frase)):
        if ord(frase[i]) >= 65 and ord(frase[i]) <= 90:
            string += str(frase[i])
    return string