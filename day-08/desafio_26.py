frase = str(input('Digite uma frase: ').strip())
frase_maiuscula = frase.upper()
qto_a = frase_maiuscula.count('A')
primeira_posicao = frase_maiuscula.find('A')
ultima = frase_maiuscula[-1].find('A') + 1
ultima_posicao = len(frase) - ultima
print("""A frase digitada foi {}
Quantos vezes aparece a letra "A" {}
A primeira posição da letra "A" {}
A última posição da letra "A" {}
""".format(frase, qto_a, primeira_posicao, ultima_posicao))
print(len(frase))