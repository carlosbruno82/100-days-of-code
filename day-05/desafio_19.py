# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo 
# na tela o nome do escolhido.

from random import choice
'''
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('O segundo: '))
a3 = str(input('O terceiro: '))
a4 = str(input('E o quarto: '))
print('O sorteado entre os alunos {}, {}, {}, {} para apagar o quadro foi: {}!'.format(a1, a2, a3, a4, choice([a1, a2, a3, a4])))
'''
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))