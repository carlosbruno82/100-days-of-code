# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 
# 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai 
# custar R$7,00 por cada Km acima do limite.

vel = int(input('A velocidade percorrida do carro: '))
if vel > 80:
  multa = (vel - 80) * 7
  print('Você passou de 80km/h. Este é o valor da sua multa: R$ {:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')