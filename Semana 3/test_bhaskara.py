# Fixtures: é um valor fixo para um conjunto de testes...
# Usado para: guardar um objeto que requer um pouco mais de trabalho para ser criado...
# Para implmenetar: construimos uma função que cria o objeto e a marcamos com @pytest.fixture (linha 13-15)...

# Importando a classe 'bhaskaraClasse'
import bhaskaraClasse
import pytest

# Criando a classe 'TestBhaskara'
class TestBhaskara:
    
    # Definindo uma fixture
    @pytest.fixture
    def b(self):
        return bhaskaraClasse.Bhaskara()
    
    # Criando o método 'testa_uma_raiz' recebe 'self' como método construtor e 'b' como @pytest.fixture
    def testa_uma_raiz(self, b):
        # Teste: b.calcula_raizes(a, b, c) == (quantidade de raizes, raizes)
        assert b.calcula_raizes(1, 0, 0) == (1, 0)

    # Criando o método 'testa_duas_raizes' recebe 'self' como método construtor e 'b' como @pytest.fixture
    def testa_duas_raizes(self, b):
        # Teste: b.calcula_raizes(a, b, c) == (quantidade de raizes, raizes)
        assert b.calcula_raizes(1, -5, 6) == (2, 3, 2)

    # Criando o método 'testa_zero_raizes' recebe 'self' como método construtor e 'b' como @pytest.fixture
    def testa_zero_raizes(self, b):
        # Teste: b.calcula_raizes(a, b, c) == (quantidade de raizes, raizes)
        assert b.calcula_raizes(10, 10, 10) == (0)

    # Criando o método 'testa_raiz_negativa' recebe 'self' como método construtor e 'b' como @pytest.fixture
    def testa_raiz_negativa(self, b):
        # Teste: b.calcula_raizes(a, b, c) == (quantidade de raizes, raizes)
        assert b.calcula_raizes(10, 20, 10) == (1, -1)
