# Orientação a Objetos II

# Método especial __init__: conhecido como construtor da classe, chamado automaticamente
# pelo interpretador quando os objetos são criados (quando classes são instânciadas)...

# Self: é o primeiro elemento da classe, faz referência ao próprio objeto, passando o 
# endereço de memória onde o objeto estará armazenado...

# Construção do método especial __init__:
# class NomeClasse:
#   def __init__(self, metodo1, metodo2 ... metodoN):
#       self.atributo1 = atributo1
#       self.atributo2 = atributo2
#       self.atributoN = atributoN

# A esquerda do sinal de igualdade temos a referêcia aos parâmetros passado no def __init__
# a direita do sinal temos os valores dos atributos...


# Criando uma classe com __init__
class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

# Instânciando um objeto 'carro_antigo' na classe Carro
carro_antigo = Carro('Fuscão', 1970, 'Preto')
# Instânciando um objeto 'carro_novo' na classe Carro
carro_novo = Carro('Corolla', 2020, 'Prata')

# Mostrando os objetos instânciados
print(carro_antigo.modelo, carro_antigo.ano, carro_antigo.cor)
print(carro_novo.modelo, carro_novo.ano, carro_novo.cor)