# Escreva um programa para aprovar o empréstimo bancário para a compra 
# de uma casa. Pergunte o valor da casa, o salário do comprador e em 
# quantos anos ele vai pagar. A prestação mensal não pode exceder 30% 
# do salário ou então o empréstimo será negado.

casa = float(input('Valor da casa? R$ '))
salario = float(input('Salário do comprador? R$ '))
ano = int(input('Quantos anos de financiamento? '))
trinta = salario * 30 / 100
prestacao = casa / (ano * 12)

print('Para pagar uma casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}'.format(casa, ano, prestacao))

if prestacao <= trinta:
  print('Empréstimo pode ser CONCEDIDO!')
else:
  print('Empréstimo NEGADO!')

