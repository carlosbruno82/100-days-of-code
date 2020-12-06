n1 = float(input('Primeira nota? '))
n2 = float(input('Segunda nota? '))
media = (n1 + n2) / 2

if media < 5:
  print('Sua média foi {}'.format(media))
  print('Reprovado.')
elif media <= 6.9:
  print('Sua média foi {}'.format(media))
  print('Recuperação.')
elif media >= 7:
  print('Sua média foi {}'.format(media))
  print('Aprovado.')