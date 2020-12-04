# Escreva um programa que faça o computador "pensar" em um número 
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi 
# o número escolhido pelo computador. O programa deverá escrever na 
# tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

user = int(input('Escolha um número entre 0 e 5: '))
cpu = randint(0,5)

print('PROCESSANDO...')
sleep(2)
if user == cpu:
  print('Venceu! Seu número é igual do CPU: {}'.format(cpu))
else:
  print('Perdeu! Seu número não é igual do CPU: {}'.format(cpu))