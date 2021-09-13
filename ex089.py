''' CRIE UM PROGRAMA QUE LEIA NOME E DUAS NOTAS DE VÁRIOS ALUNOS E GUARDE TUDO EM UMA LISTA COMPOSTA.
NO FINAL MOSTRE UM BOLETIM CONTENDO A MÉDIA DE CADA UM E PERMITA QUE O USUÁRIO POSSA
MOSTRAR AS NOTAS DE CADA ALUNO INDIVIDUALMENTE'''
from time import sleep
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"Nome":<10}{"Média:":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:<8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar nota de qual aluno? 999 para interromper: '))
    if opc == 999:
        for i, a in enumerate('Finalizando ... '):
            print(f'{a}', end='')
            sleep(0.05)
        print()
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
for i, a in enumerate('<<< Volte Sempre... >>>'):
    print(f'{a}', end='')
    sleep(0.05)