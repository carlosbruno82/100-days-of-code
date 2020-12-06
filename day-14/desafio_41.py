from datetime import date

nascimento = int(input('Ano de nascimento? '))
idade = date.today().year - nascimento

if idade <= 9:
  print('Mirin')
elif idade <= 14:
  print('Infatil')
elif idade <= 19:
  print('Júnior')
elif idade <= 20:
  print('Sênior')
else:
  print('Master')