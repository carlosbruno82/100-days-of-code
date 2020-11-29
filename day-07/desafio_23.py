num = int(input('digite um número: ').strip())
numero = num
unidade =  num % 10
num = (num - unidade) / 10
dezena = num % 10
num = (num - dezena) / 10
centena = num % 10
num = (num - centena) / 10
milhar = num

print("""Número digitado: {}
Sua unidade: {}
Sua dezena: {}
Sua centena: {}
Sua milhar: {}""".format(numero, unidade, int(dezena), int(centena), int(milhar)))