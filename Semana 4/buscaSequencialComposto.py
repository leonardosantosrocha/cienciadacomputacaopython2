# Busca sequencial composto

# Criando a classe 'Musica'
class Musica:
    # Criando um método '__init__' que recebe 'self' como construtor e os demais parâmeteros
    def __init__(self, titulo, interprete, compositor, ano):
        self.titulo = titulo
        self.interprete = interprete
        self.compositor = compositor
        self.ano = ano

# Criando a classe 'Buscador'
class Buscador:
    # Criando um método 'busca_por_titulo' que recebe 'self' como construtor e os demais parâmetros
    def busca_por_titulo(self, playlist, titulo):
        # Criando uma laço para percorrer e realizar a busca sequencial
        for i in range(len(playlist)):
            # Verificando se o título atual é igual ao titulo buscado
            if playlist[i].titulo == titulo:
                # Retornando o título
                return titulo
        # Retornando -1
        return -1

    # Criando um método 'vamos_buscar' que recebe 'self' como construtor
    def vamos_buscar(self):
        # Criando uma lista de músicas
        playlist = [ Musica("Música I", "Cantor I", "Compositor I", 2019),
                     Musica("Música II", "Cantor II", "Compositor II", 2020),
                     Musica("Música III", "Cantor III", "Compositor III", 2021)]
        
        # Armazenando o método 'busca_por_titulo' que recebe playlist e música buscada na variável 'onde_achou'
        onde_achou = self.busca_por_titulo(playlist, "Música I")

        # Caso a música não seja encontrada
        if onde_achou == -1:
            # Mensagem para o usuário
            print('Minha música preferida não está na playlist')
        # Caso a música seja encontrada
        else:
            preferida = playlist[onde_achou]
            print(preferida.titulo, preferida.interprete, preferida.compositor, preferida.ano, sep=', ')

b = Buscador()
b.vamos_buscar()