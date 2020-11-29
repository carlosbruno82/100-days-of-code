nome = str(input('Digite o nome completo: ').strip())

nome_caps = nome.upper()

nome_low = nome.lower()

nome_lista = nome.split()

nome_junto = ''.join(nome_lista)

nome_total = len(nome_junto.strip())

primeiro_nome = len(nome_lista[0])

print("""
Bem vindo(a) {}.
Seu nome em maiúsculo: {}
Seu nome em minúsculo: {}
Total de letras do seu nome: {}
Total de letras do primeiro nome: {}
""".format(nome, nome_caps, nome_low, nome_total, primeiro_nome))