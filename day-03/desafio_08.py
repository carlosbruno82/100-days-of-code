# Escreva um programa que leia um valor em metros e o exiba convertido
#em centímetros e milimetros.

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A média de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))