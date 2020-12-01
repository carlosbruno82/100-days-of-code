cidade = str(input('Digite o nome da cidade: ').strip())
cidade_caps = cidade.upper()
cidade_lista = cidade_caps.split()
santo = 'SANTO' in cidade_lista[0]
print("""O nome da cidade é: {}
Primeiro nome é Santo? {}""".format(cidade, santo))
