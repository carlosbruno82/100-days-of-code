from random import choice
from time import sleep

jogador = str(input('pedra, papel ou tesoura? ')).lower().strip()
jokenpo = ['pedra', 'papel', 'tesoura']
computador = choice(jokenpo)

print('Jo..')
sleep(1)
print('ken..')
sleep(1)
print('pô..')
sleep(1)

if jogador == 'tesoura' and computador == 'papel':
  print('Jogador: {} e Computador: {}'.format(jogador, computador))
  print('Você ganhou!')
elif jogador == 'pedra' and computador == 'tesoura':
  print('Jogador: {} e Computador: {}'.format(jogador, computador))
  print('Você ganhou!')
elif jogador == computador:
  print('Jogador: {} e Computador: {}'.format(jogador, computador))
  print('Empate!')
else:
  print('Jogador: {} e Computador: {}'.format(jogador, computador))
  print('Você Perdeu!')