# Faça um programa que leia um ângulo qualquer e mostre na tela o valor 
# do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
coss = cos(radians(angulo))
tang = tan(radians(angulo))
print('O ângulo de {} tem o SENO {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o COSSENO {:.2f}'.format(angulo, coss))
print('O ângulo de {} tem o TANGENTE {:.2f}'.format(angulo, tang))