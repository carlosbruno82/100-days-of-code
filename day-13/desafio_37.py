n = int(input('Digite um número inteiro: '))
c = int(input('Escolha a conversão: "1" para binário, "2" para octal, "3" para hexadecimal: '))

if c == 1:
  print('O número digitado em binário: {}'.format(bin(n)))
elif c == 2:
  print('O número digitado em em octal: {}'.format(oct(n)))
elif c == 3:
  print('O número digitado em Hexadecimal: {}'.format(hex(n)))
else:
  print('Opção inválida.')