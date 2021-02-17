# Caracteres de uma string
paisagem = 'rio'
# Leitura da esquerda para direita
print(paisagem[0], paisagem[1], paisagem[2])
# Leitura da direita para esquerda
print(paisagem[-1], paisagem[-2], paisagem[-3])

# Convertendo tudo para maiúsculo
nome = 'leonardo'
print(nome.upper())

# Convertendo tudo para minúsculo
nome = 'LEONARDO'
print(nome.lower())

# Convertendo a primeira letra da frase em maiúscula
frase = 'leonardo gosta de video-games'
print(frase.capitalize())

# Removendo espaços antes ou depois da palavra
email = '   leonardo@email.com   '
print(email.strip())

# Quantidade de caracteres específico em uma palavra
cidade = 'Barueri'
print(cidade.count('r'))

# Substituir palavra em uma string
time = 'Eu torço para o Palmeiras'
print(time.replace('Palmeiras', 'Corinthians'))

# Centralizar textos
frase = 'Eu irei tomar uma casquinha'
print(frase.center(100))

# Encontrar a primeira ocorrência de um texto
musica = 'Dont live too fast, troubles will come and they will pass'
print(musica.find('live'))

# Slice ou pedaços de strings
fruta = 'Amora'
print(fruta[0:4])