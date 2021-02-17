# Crie um programa para contar as vogais ou consoantes de uma frase, caso não passe o segundo parâmetro contará automaticamente as vogais
def conta_letras(frase, contar="vogais"):
    # Variáveis para acumular
    vogais = 0
    consoantes = 0
    # Laço para as vogais
    if contar == 'vogais':
        for i in range(len(frase)):
            if frase[i] == 'a' or frase[i] == 'e' or frase[i] == 'i' or frase[i] == 'o' or frase[i] == 'u':
                vogais += 1
        return vogais
    # Laço para as consoantes
    else:
        for i in range(len(frase)):
            if frase[i] != 'a' and frase[i] != 'e' and frase[i] != 'i' and frase[i] != 'o' and frase[i] != 'u' and frase[i] != ' ':
                consoantes += 1
        return consoantes