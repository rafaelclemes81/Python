''' DESENVOLVAR UM PROGRAMA QUE LEIA QUATRO VALORES PELO TECLADO E GUARDE-OS NUMA TUPLA.
NO FINAL MOSTRE:
A - QUANTAS VEZES APARECEU O NÚMERO 9
B - EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3
C - QUAIS FORAM OS NÚMEROS PARES'''
"""n1 = int(input('Informe o 1º número: '))
n2 = int(input('Informe o 2º número: '))
n3 = int(input('Informe o 3º número: '))
n4 = int(input('Informe o 4º número: '))"""
t = (int(input('Informe o 1º número: ')),
     int(input('Informe o 1º número: ')),
     int(input('Informe o 1º número: ')),
     int(input('Informe o 1º número: ')))
if 9 in t:
    print(f'O número 9 foi informado {t.count(9)} vezes.')
else:
    print('O número 9 não foi informado.')
if 3 in t:
    print(f'O número 3 está na posição {t.index(3)+1} da tupla.')
else:
    print('O número 3 não foi informado.')
print(f'Os números pares informados foram: ', end=' ')
for i in range(0, 4):
    if t[i] % 2 == 0:
        print(t[i], end=' ')

