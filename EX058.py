''' MELHORE O JOGO DO DESAFIO 028 ONDE O PC VAI 'PENSAR' UM NÚMERO ENTRE 0 E 10.
SÓ QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR ATÉ ACERTAR, MOSTRANDO NO FINAL QUANTOS PALPITES FORAM
NECESSÁRIOS PARA VENCER'''
from random import randint
r = randint(0, 10)
c = 1
n = int(input('Em que número eu pensei? '))
while n != r:
    c += 1
    n = int(input('Tente outra vez. Em que número eu pensei? '))
print('Você acertou depois de {} tentativas.'.format(c))


