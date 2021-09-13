"""escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
peça para o usuário tentar descobrir qual foi o número "pensado" pelo computador
	o programa deverá escrever na tela se o usuário venceu ou perdeu"""

from random import randint
from time import sleep
n = randint(0, 5)
r = int(input('Em que número você acha que o computador pensou ?'))
print('PROCESSANDO ... ')
sleep(3)
if r == n:
    print('Você acertou, o número pensado pelo computador foi {}'.format(n))
else:
    print('Que pena, não foi dessa vez. O computador pensou no número {} '.format(n))
    print('Tente outra vez')