s = float(input('Salário do funcionário? '))
if s > 1250:
  aumento = s + (s * 10 / 100 )
  print('O salário com aumento de 10% R$ {:.2f}'.format(aumento))
else:
  aumento = s + (s * 15 / 100)
  print('O salário com aumento de 15% R$ {:.2f}'.format(aumento))