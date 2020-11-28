from random import choice

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('O segundo: '))
a3 = str(input('O terceiro: '))
a4 = str(input('E o quarto: '))
print('O sorteado entre os alunos {}, {}, {}, {} para apagar o quadro foi: {}!'.format(a1, a2, a3, a4, choice([a1, a2, a3, a4])))