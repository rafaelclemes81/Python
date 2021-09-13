''' FAÇA UM PROGRAMA QUE JOGUE PAR OU ÍMPAR COM O COMPUTADOR. O JOGO SÓ SERÁ INTERROMPIDO QUANDO O
JOGADOR PERDER, MOSTRANDO O TOTAL DE VITÓRIAS CONSECUTIVAS QUE ELE CONQUISTOU AO FINAL DO PROGRAMA'''
from random import randint
jogada = ' '
v = 0
while True:
    jogador = int(input('Informe um número entre 0 e 10: '))
    while jogada not in 'PI':
        jogada = str(input('Qual sua jogada [P/I] ?').strip().upper())[0]
    computador = randint(0, 10)
    print(f'Computador escolheu {computador}')
    if  (jogador + computador) % 2 == 0:
        if jogada == 'P':
            print('Parabéns. Você venceu!!! Vamos jogar novamente...')
            v += 1
    else:
        print('GAME OVER... ')
        break
    jogada = ' '
print(f'Você venceu {v} vezes. Fim de jogo ....')




