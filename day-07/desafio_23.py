# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um 
# dos dígitos separados.


# num = int(input('digite um número: ').strip())
# numero = num
# unidade =  num % 10
# num = (num - unidade) / 10
# dezena = num % 10
# num = (num - dezena) / 10
# centena = num % 10
# num = (num - centena) / 10
# milhar = num

# print("""Número digitado: {}
# Sua unidade: {}
# Sua dezena: {}
# Sua centena: {}
# Sua milhar: {}""".format(numero, unidade, int(dezena), int(centena), int(milhar)))

# OR
num = int(input('digite um número: ').strip())
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print("""Número digitado: {}
Sua unidade: {}
Sua dezena: {}
Sua centena: {}
Sua milhar: {}""".format(num, u, d, c, m))