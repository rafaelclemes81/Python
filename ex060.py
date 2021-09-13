''' FAÇA UM PROGRAMA QUE LEIA UM NÚMERO E MOSTRE SEU FATORIAL'''
from time import sleep
n = int(input('Informe um número inteiro: '))
c = n
f = 1
print('Calculando o fatorial de {}!'.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    sleep(0.2)
    f *= c
    c -= 1
print('{}'.format(f))
