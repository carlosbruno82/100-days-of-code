# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
# quantos Dólares ela pode comprar.
# Considere US$ 1.00 = R$ 3.27

real = float(input('Quanto dinheiro você na carteira? R$ '))
dolar = real / 3.27
print('com R$ {:.2f} você pode comprar U$ {:.2f}'.format(real, dolar))