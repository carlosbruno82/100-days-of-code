produto = float(input('Qual o preço do produto? '))
pagamento = int(input("""Condição do pagamento: 
Digite "1" à vista no dinheiro/cheque
Digite "2" à vista no cartão
Digite "3" em até 2 vezes no cartão
Digite "4" em até 3 vezes ou mais no cartão 
: """))

if pagamento == 1:
  print('O valor do produto com 10{} de desconto é R$ {}'.format('%', produto - (produto * 10 / 100)))
elif pagamento == 2:
  print('O valor do produto com 5{} de desconto é R$ {}'.format('%', produto - (produto * 5 / 100)))
elif  pagamento == 3:
  print('O valor do produto é R$ {}'.format(produto))
elif pagamento == 4:
  print('O valor do produto com 20{} de juros é R$ {}'.format('%', produto + (produto * 20 / 100)))
else:
  print('Opção inválida!')
  

