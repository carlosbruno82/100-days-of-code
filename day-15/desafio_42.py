a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))

r1 = (b - c) < a < b + c
r2 = (a - c) < b < a + c
r3 = (a - b) < c < a + b

if r1 and r2 and r3:
  print('Podem formar um triângulo')
  if a == b and a == c:
    print('Equilátero: todos os lados iguais')
  elif a == b and a != c or b != a and b == c:
    print('Isósceles: dois lados iguais')
  elif a != b and a != c and b != c:
    print('Escaleno: todos os lados diferentes')
else:
  print('Não podem formar um triângulo')