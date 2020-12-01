#Crie um programa que leia o nome de uma pessoa e diga se 
# ela tem "SILVA" no nome.

nome = str(input('Digite o nome: ').strip())
nome_lista = 'silva' in nome.lower()
print('Possui Silva no nome: {}.'.format(nome_lista))