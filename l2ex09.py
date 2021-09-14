'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''
num = list()
for i in range(0,3):
    n = int(input(f'Informe o {i+1}º número: '))
    num.append(n)
num.sort()
for i, n in enumerate(num):
    if i+1 < len(num):
        print(f'{n} - ', end='')
    else:
        print(f'{n}', end='')
