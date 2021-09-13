'''O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
 Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''
from random import shuffle
a1 = str(input('Informe o primeiro aluno: '))
a2 = str(input('Informe o segundo aluno: '))
a3 = str(input('Informe o terceiro aluno: '))
a4 = str(input('Informe o quarto aluno: '))
alunos = [a1, a2, a3, a4]
shuffle(alunos)
print('A ordem de apresentação dos trabalhos é:')
print(alunos)
