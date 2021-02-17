# Orientação a Objetos I

# Objeto: dado + código, logo é um dado encapsulado, evitando que códigos de 
# um objeto específico se comuniquem e interfiram com códigos de outro objeto.
# 
# Classes: definem os tipos dos objetos; definem quais os dados e o código 
# (funções) dos objetos;
# 
# Dados: são os atributos da classe ou objeto
# Código: são os métodos da classe ou objeto
# Objetos são chamados de instâncias das classes


# Criando uma classe
class Carro:
    pass

# Instânciando objetos: objeto instânciando = Classe()
meu_carro = Carro()
carro_da_fci = Carro()

# Adicionando atributos a classe carro
meu_carro.ano = 2020
meu_carro.modelo = 'Madza RX7'
meu_carro.cor = 'Preto'

# Adicionando atributos a classe carro
carro_da_fci.ano = 2020
carro_da_fci.modelo = 'GTR'
carro_da_fci.cor = 'Prata'

