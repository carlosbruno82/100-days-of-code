from datetime import date

atual = date.today().year
print('''Escolha o sexo:
[1] Homem
[2] Mulher''')
sexo = int(input('Opção: '))

if sexo == 2:
  print('Não precisa se alistar.')
else:
  nasc = int(input('Ano de nascimento: '))
  idade = atual - nasc
  print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

  if idade == 18:
    print('Você tem que se alistar IMEDIAMENTE!')
  elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
  else:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
