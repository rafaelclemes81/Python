''' REFAÇA O DESAFIO 051, LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA P.A. MOSTRANDO OS 10
PRIMEIROS TERMOS DA PROGRESSÃO USANDO A ESTRUTURA WHILE'''
from time import sleep
n = int(input('Informe um número: '))
r = int(input('Informe a razão da P.A: '))
c = 1
while c <= 10:
    sleep(0.1)
    print(n, end=' ')
    n += r
    c += 1
print('|')