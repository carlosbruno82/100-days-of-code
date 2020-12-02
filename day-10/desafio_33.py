n1 = int(input('Primeiro número:'))
n2 = int(input('Segundo número:'))
n3 = int(input('Terceiro número:'))
if n1 < n2 and n1 < n3 and n2 > n3:
  print('Menor: {}, Maior: {}'.format(n1, n2))
if n1 < n2 and n1 < n3 and n3 > n2:
  print('Menor: {}, Maior: {}'.format(n1, n3))

if n2 < n1 and n2 < n3 and n1 > n3:
  print('Menor: {}, Maior: {}'.format(n2, n1))
if n2 < n1 and n2 < n3 and n3 > n1:
  print('Menor: {}, Maior: {}'.format(n2, n3))
  
if n3 < n1 and n3 < n2 and n1 > n2:
  print('Menor: {}, Maior: {}'.format(n3, n1))
if n3 < n1 and n3 < n2 and n2 > n1:
  print('Menor: {}, Maior: {}'.format(n3, n2))


