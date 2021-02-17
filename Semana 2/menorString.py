# Crie uma função que recebe uma lista de nomes e retorna o menor capitalizado e sem espaços
def menor_nome(palavras):
    for i in range(len(palavras)):
        string = str(palavras[i]).strip().capitalize()
        if len(string) < len(palavras[0]):
            return string
    return 'Zé'
print(menor_nome(['maria', 'josé', 'PAULO', 'Catarina']))
# deve devolver 'José'

print(menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ']))
# deve devolver 'José'

print(menor_nome(['Bárbara', 'JOSÉ  ', 'Bill']))
# deve devolver José

print(menor_nome(['zé', ' lu', 'fê']))
# deve devolver José
