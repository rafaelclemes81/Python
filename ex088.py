''' FAÇA UM PROGRAMA QUE AJUDE UM JOGADOR A CRIAR PALPITES. O PROGRAMA VAI PERGUNTAR
QUANTOS JOGOS SERÃO GERADOS, E VAI SORTEAR 6 NÚMEROS ENTRE 1 E 60 PARA CADA JOGO
CADASTRANDO TUDO EM UMA LISTA COMPOSTA'''
from random import randint
from time import sleep
mega = []
palpite = randint(1, 60)
jogos = int(input('Quantos jogos deseja criar? '))
for i in range(0, jogos):
    mega.append([])
    for j in range (0,6):
        while True:
            if palpite in mega[i]:
                palpite = randint(1, 60)
            else:
                break
        mega[i].append(palpite)
    mega[i].sort()
    print(f'{mega[i]}')
    sleep(1)
