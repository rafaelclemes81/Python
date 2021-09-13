''' MELHORE O DESAFIO 061, PERGUNTANDO PARA O USUÁRIO QUANTOS TERMOS DA P.A. ELE QUER
QUE SEJAM MOSTRADOS. O PROGRAMA TERMINA SE '0' FOR INFORMADO
'''
from time import sleep
n = int(input('Informe um número: '))
r = int(input('Informe a razão da P.A: '))
resp = int(input('Quantos elementos da P.A você quer exibir? '))
c = 1
while c <= resp:
    sleep(0.2)
    print(n, end=' ')
    n = n + r
    c += 1