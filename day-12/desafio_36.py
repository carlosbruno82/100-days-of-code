c = float(input('Qual o valor da casa? '))
s = float(input('Quanto você recebe por mês? '))
a = int(input('Quantos anos pretende pagar a casa? '))
t = s * 30 / 100
p = c / (a * 12)
print('Valor da casa: R$ {:.2f}'.format(c))
print('Salário mensal: R$ {:.2f}'.format(s))
print('Valor da prestação mensal: R$ {:.2f}'.format(p))
print('{} do salário: R$ {:.2f}'.format('30%', t))


if p < t:
  print('O empréstimo poderá ser realizado.')
elif p > t:
  print('O empréstimo não poderá se realizado.')

