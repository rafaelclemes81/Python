'''ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA A QUANTIDADE DE
ELEMENTO DA SEQUENCIA FEBONACCI QUE O USUÁRIO SOLICITAR'''
from time import sleep
e = int(input('Quantos elementos da série Febonacci você quer exibir? '))
i = 4
a = 0
b = 1
c = a + b
print(a, end=' ')
sleep(0.2)
print(b, end=' ')
sleep(0.2)
print(c, end=' ')
sleep(0.2)
while i <= e:
    a = b
    b = c
    c = a + b
    print((c), end=' ')
    sleep(0.2)
    i += 1
