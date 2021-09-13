from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Sua opções: 
[0]-Pedra
[1]-Papel
[2]-Tesoura''')
jogador = int(input('Escolha uma jogada: '))
print('{:^28}'.format('JO'))
sleep(1)
print('{:^28}'.format('KEN'))
sleep(1)
print('{:^28}'.format('PO'))
print('-='*14)
print('Computador escolheu {}'.format(itens[computador]))
print('Jogador escolheu {}'.format(itens[jogador]))
print('-='*14)
if computador == 0:
    if jogador == 0:
        print('Não houve vencedor.')
    elif jogador == 1:
        print ('Jogador venceu. Papel embrulha a pedra. ')
    elif jogador == 2:
        print('Computador Venceu. Pedra quebra a tesoura.')
    else:
        print('Jogada Inválida...')
elif computador == 1:
    if jogador == 1:
        print('Não houve vencedor.')
    elif jogador == 0:
        print ('Computador venceu. Papel embrulha a pedra. ')
    elif jogador == 2:
        print('Jogador Venceu. Tesoura corta o papel.')
    else:
        print('Jogada Inválida...')
elif computador == 2:
    if jogador == 2:
        print('Não houve vencedor.')
    elif jogador == 0:
        print ('Jogador venceu. Pedra quebra a tesoura. ')
    elif jogador == 1:
        print('Computador Venceu. Tesoura corta o papel.')
    else:
        print('Jogada Inválida...')
