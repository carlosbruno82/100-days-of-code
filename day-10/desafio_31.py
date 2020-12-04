# esenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens 
# de até 200Km e R$0,45 parta viagens mais longas.

d = int(input('Qual a distância da viagem em km? '))
if d <= 200:
  print('O valor da passagem será R$ {:.2f}'.format(d * 0.50))
else:
  print('O valor da passagem será R$ {:.2f}'.format(d * 0.45))