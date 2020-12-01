nome = str(input('Digite o nome: ').strip())
nome_lista = nome.split()
primeiro_nome = nome_lista[0]
ultimo_nome = nome_lista[-1]
print("""Olá {}
Seu primeiro nome é: {}
Seu último nome é: {}
""".format(nome, primeiro_nome, ultimo_nome))