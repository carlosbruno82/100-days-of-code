# Escreva um programa que pergunte o salário de um funcionário e calcule o 
# valor do seu aumento. Para salários superiores a R$1250,00, calcule um 
# aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

s = float(input('Salário do funcionário? '))
if s > 1250:
  aumento = s + (s * 10 / 100 )
  print('O salário com aumento de 10% R$ {:.2f}'.format(aumento))
else:
  aumento = s + (s * 15 / 100)
  print('O salário com aumento de 15% R$ {:.2f}'.format(aumento))