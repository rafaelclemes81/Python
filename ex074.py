''' CRIE UM PROGRAMA QUE VAI GERAR CINCO NÚMEROS ALEATÓRIOS E COLOCAR EM UMA TUPLA.
DEPOIS DISSO, MOSTRE A LISTAGEM DE NÚMEROS GERADOS E TAMBÉM INDIQUE O MENOR O MAIOR VALOR QUE ESTÃO NA TUPLA.'''
from random import randint
t = randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10)
print(f'Os números gerados foram : {t}')
"""maior = 0
menor = 11
for i in range (0, 5):
    if t[i] > maior:
        maior = t[i]
    if t[i] < menor:
        menor = t[i]
print(f'O maior número gerado foi {maior} e o menor foi {menor}.')"""
print(f'O maior valor gerado foi {max(t)}')
print(f'O menor valor gerado foi {min(t)}')
print('Fim do programa ... ')
