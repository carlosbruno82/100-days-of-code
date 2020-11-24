n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
r = n1 % n2
# end= Continua na mesma linha
# \n Quebra de linha
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' >>> ')
print('Divisão inteira é {}, a potencia é {} e o resto da divisão é {}'.format(di, p, r))