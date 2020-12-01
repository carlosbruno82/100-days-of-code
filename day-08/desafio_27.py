# Faça um programa que leia o nome completo de uma pessoa, mostrando 
# em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o nome: ').strip())
nome_lista = nome.split()
primeiro_nome = nome_lista[0]
ultimo_nome = nome_lista[-1]
print("""Muito prazer em te conhecer!
Seu primeiro nome é: {}
Seu último nome é: {}
""".format(primeiro_nome, ultimo_nome))