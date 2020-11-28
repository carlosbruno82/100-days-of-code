# O mesmo professor do desafio 019 quer sortear a ordem de apresentação 
# de trabalhos dos alunos. Faça um programa que leia o nome dos quatro 
# alunos e mostre a ordem sorteada.

from random import shuffle

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('O segundo: '))
a3 = str(input('O terceiro: '))
a4 = str(input('E o quarto: '))
alunos = [a1, a2, a3, a4] 
shuffle(alunos)
print('A ordem sorteada dos alunos para apresentação de trabalhos: {}!'.format(alunos))