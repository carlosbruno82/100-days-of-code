# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).


nome = str(input('Digite seu nome completo: ').strip())

nome_caps = nome.upper()

nome_low = nome.lower()

nome_lista = nome.split()

nome_junto = ''.join(nome_lista)

nome_total = len(nome_junto)

primeiro_nome = nome_lista[0]

primeiro_nome_total = len(nome_lista[0])

print("""
Bem vindo(a) {}.
Seu nome em maiúsculo é {}
Seu nome em minúsculo é {}
Seu nome tem ao todo {} letras
Seu primeiro nome é {} e ele tem {} letras
""".format(nome, nome_caps, nome_low, nome_total, primeiro_nome, primeiro_nome_total))