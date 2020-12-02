ano = int(input('Digite um ano qualquer: '))
if ano % 4 == 0 and ano % 100 != 0:
  print('Este ano é bissexto')
else:
  print('Este ano não é bissexto')