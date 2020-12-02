vel = int(input('A velocidade percorrida do carro: '))
if vel > 80:
  multa = (vel - 80) * 7
  print('Você passou de 80km/h. Este é o valor da sua multa: R$ {:.2f}'.format(multa))