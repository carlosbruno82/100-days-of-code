from random import randint

user = int(input('Escolha um número entre 0 e 5: '))
cpu = randint(0,5)
if user == cpu:
  print('Venceu! Seu número é igual do CPU: {}'.format(cpu))
else:
  print('Perdeu! Seu número não é igual do CPU: {}'.format(cpu))