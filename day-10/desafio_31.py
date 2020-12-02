d = int(input('Qual a distância da viagem em km? '))
if d <= 200:
  print('O valor da passagem será R$ {:.2f}'.format(d * 0.50))
else:
  print('O valor da passagem será R$ {:.2f}'.format(d * 0.45))