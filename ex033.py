"""faça um programa que leia 3 número inteiros e diga qual é o maior e qual é o menor"""
n1 = int(input('Informe o primeiro número: '))
ma = n1
me = n1
n2 = int(input('Informe o segundo número: '))
if n2 > ma:
    ma = n2
    if n2 < me:
        me = n2;
else:
    if n2 < me:
        me = n2
n3 = int(input('Informe o terceiro número: '))
if n3 > ma:
    ma = n3
    if n3 < me:
        me = n3;
else:
    if n3 < me:
        me = n3
print('O maior número informado foi {} e o menor foi {}.'.format(ma, me))

