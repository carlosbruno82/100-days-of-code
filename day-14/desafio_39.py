from datetime import date

nascimento = int(input('Qual o ano de nascimento? '))
idade = date.today().year - nascimento

if idade < 18:
  print('Ainda vai se alistar.')
  if 18 - idade == 1:
    print('Falta {} ano para se alistar.'.format(18 - idade))
  else:
    print('Falta {} anos para se alistar.'.format(18 - idade))
elif idade == 18:
  print('Hora de se alistar.')
elif idade > 18:
  print('Passou do tempo ')
  if idade - 18 == 1:
    print('Já passou {} ano para alistamento.'.format(idade - 18))
  else:
    print('Já passou {} anos para alistamento.'.format(idade - 18))