from math import hypot

oposto = float(input('Número do cateto oposto: '))
adjacente = float(input('Número do cateto adjacente: '))
print('O comprimento da hipotenusa é {}'.format(hypot(oposto, adjacente)))