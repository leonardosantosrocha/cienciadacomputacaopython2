# Crie o programa do elefantinho
def incomodam(n):
    if n < 1:
        return ''
    else:
        return 'incomodam ' + incomodam(n-1)

def elefantes(n, primeira_vez = True):
    frase = ''

    if n <= 0:
        return ''

    if n == 1:
        return 'Um elefante incomoda muita gente\n'

    if n >= 2:
        frase = elefantes(n-1) + str(n) + ' elefantes ' + incomodam(n) + 'muito mais' + '\n' + str(n) + ' ' + 'elefantes incomodam muita gente' + '\n'
    return frase

print(elefantes(4))