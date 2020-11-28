# Faça um programa que leia o comprimento do cateto oposto e do cateto 
# adjacente de um triângulo retângulo. Calcule e mostre o comprimento 
# da hipotenusa.

from math import hypot

oposto = float(input('Número do cateto oposto: '))
adjacente = float(input('Número do cateto adjacente: '))
hi = hypot(oposto, adjacente)
print('O comprimento da hipotenusa é {:.2f}'.format(hi))


'''
# sem módulo
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
'''