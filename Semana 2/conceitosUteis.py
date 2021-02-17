# Atribuição múltipla de valores
nome, sobrenome = 'Leonardo', 'Rocha'
print(nome, sobrenome)

# Atribuição múltipla de valores através de funções
def cidade_estado():
    return 'Barueri', 'São Paulo'
cidade, estado = cidade_estado()
print(cidade, estado)

# Inversão de variáveis
nome, sobrenome = 'Leonardo', 'Rocha'
nome, sobrenome = sobrenome, nome
print(nome, sobrenome)

# Atribuição aumentada (x = x + 10) == (x += 10)
n = 10
n += 10
print(n)

# Subtração aumentada (x = x - 10) == (x -= 10)
n = 20
n -= 10
print(n)

# Multiplicação aumentada (x = x * 10) == (x *= 10)
n = 10
n *= 10
print(n)

# Divisão aumentada (x = x / 10) == (x /= 10)
n = 10
n /= 10
print(n)

# Parâmetro padrão (case não seja informado, assumirá o 120)
def pagamento_semanal_1(valorHora, numeroHoras = 120):
    return valorHora * numeroHoras
print(pagamento_semanal_1(17.5, 120))

# Asserção de invariantes
def pagamento_semanal_2(valorHora, numeroHoras = 120):
    # Asserção
    assert valorHora >= 0 and numeroHoras >= 1
    return valorHora * numeroHoras
print(pagamento_semanal_2(17.5, -1))