n = str(input('Digite seu nome: '))

# 20 espaços
print('Prazer em te conhecer {:20}!'.format(n))

# Alinhamento a direita em 20 espaço
print('Prazer em te conhecer {:>20}!'.format(n))

# Alinhamento a esqueda em 20 espaço
print('Prazer em te conhecer {:<20}!'.format(n))

# Centralizado em 20 espaço
print('Prazer em te conhecer {:^20}!'.format(n))

# Centralizado em 20 espaço com o sinal de =
print('Prazer em te conhecer {:=^20}!'.format(n))