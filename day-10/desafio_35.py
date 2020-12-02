# | b - c | < a < b + c
# | a - c | < b < a + c
# | a - b | < c < a + b

a = int(input('Primeira reta: '))
b = int(input('Segunda reta: '))
c = int(input('Terceira reta: '))

r1 = (b - c) < a < b + c
r2 = (a - c) < b < a + c
r3 = (a - b) < c < a + b

if r1 and r2 and r3 == True: # or if r1 and r2 and r3:
  print('Podem formar um triângulo')
else:
  print('Não podem formar um triângulo')