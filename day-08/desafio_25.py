nome = str(input('Digite o nome: ').strip())
nome_lista = 'silva' in nome.lower()
print('O nome é {}. \nPossui Silva no nome: {}.'.format(nome, nome_lista))