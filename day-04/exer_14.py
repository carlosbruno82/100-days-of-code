# Escreva um programa que converta uma temperatura digitando em graus Celsius
# e converta para graus Fahrenheit.

temperatura = float(input('Informe a temperatura em °C: '))
fahrenheit = ((temperatura * 9) / 5) + 32
#fahrenheit = temperatura * 9 / 5 + 32
print('A temperatura de {}°C corresponde a {}°F!'.format(temperatura, fahrenheit))