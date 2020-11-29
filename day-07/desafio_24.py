cidade = str(input('Digite o nome da cidade: ').strip())
cidade_caps = cidade.upper()
cidade_lista = cidade_caps.split()
santo = cidade_lista[0].find('SANTO')
print("""O nome da cidade é: {}
Primeiro nome é Santo? {}
Se o resultado for 0 é sim
Se o resultado for -1 é não 
""".format(cidade, santo))
