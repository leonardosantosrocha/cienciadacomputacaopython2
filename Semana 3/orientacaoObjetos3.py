# Criando uma função para executar o programa
def main():
    # Instânciando dois objetos 'carro1' e 'carro2' na classe 'Carro'
    carro1 = Carro('brasilia', 1970, 'amarela', 80)
    carro2 = Carro('fuscão', 1980, 'preto', 95)
    # Atribuindo os atributos aos objetos 'carro1' e 'carro2'
    carro1.acelere(40)
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()
    carro2.acelere(100)

# Criando a classe 'Carro'
class Carro:
    # Definindo o '__init__' com o método construtor 'self' e os demais métodos 'modelo', 'ano', 'cor' e 'velocidadeMax'
    def __init__(self, modelo, ano, cor, velocidadeMax):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.vel = 0
        self.velMax = velocidadeMax

    # Criando uma função com o parâmetro 'self' da classe 'Carro'
    def imprima(self):
        # Se velocidade referenciada por 'self' for igual a zero
        if self.vel == 0:
            # Mostre o 'modelo', 'cor' e 'ano' referenciados através do 'self'
            print('%s %s %d'%(self.modelo, self.cor, self.ano))
        # Se a velocidade atual for menor que a velocidade máxima referenciada por 'self'
        elif self.vel < self.velMax:
            # Mostre o 'modelo', 'cor' e 'velocidade' referenciados através do 'self'
            print('%s %s indo a %d Km/h'%(self.modelo, self.cor, self.vel))
        # Se não
        else:
            # Mostre 'modelo' e 'cor' referenciados através do 'self'
            print('%s %s indo muito rapido!'%(self.modelo, self.cor))

    # Criando a função acelere que recebe o método construtor 'self' e o parâmetro 'velocidade'
    def acelere(self, velocidade):
        # Atributo 'vel' referenciado no método construtor 'self' recebe a velocidade passada pelo parâmetro
        self.vel = velocidade
        # Se velocidade for maior que velocidade máxima referenciada pelo 'self'
        if self.vel > self.velMax:
            # Velocidade atual é igual a velocidade máxima referenciada pelo 'self'
            self.vel = self.velMax
        # Chamando a função imprima
        self.imprima()

    # Criando a função pare que recebe o construtor 'self'
    def pare(self):
        # Atributo vel referenciado no método construtor 'self' recebe o valor zero
        self.vel = 0
        # Chamando a função imprima
        self.imprima()

# Executando a função main()
main()