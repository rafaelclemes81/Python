'''CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:
[1]-SOMAR
[2]-MULTIPLICAR
[3]-MAIOR
[4]-NOVOS NÚMEROS
[5]-SAIR DO PROGRAMA

SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇÃO SOLICITADA EM CASA CASO'''
from time import sleep
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo  número: '))
vc = 0
while vc != 5:
    print('''[1]-SOMAR
[2]-MULTIPLICAR
[3]-MAIOR
[4]-NOVOS NÚMEROS
[5]-SAIR DO PROGRAMA''')
    vc = int(input('Escolha uma operação: '))
    if vc == 1:
        rs = n1 + n2
        print('A soma {} + {} = {}'.format(n1, n2, rs))
    elif vc == 2:
        rs = n1 * n2
        print('O produto {} * {} = {}'.format(n1, n2, rs))
    elif vc == 4:
        n1 = int(input('Informe o primeiro número: '))
        n2 = int(input('Informe o segundo  número: '))
    elif vc == 3:
        if n1 > n2:
            rs = n1
            print('O maior número entre {} e {} é {}'.format(n1, n2, rs))
        else:
            rs = n2
            print('O maior número entre {} e {} é {}'.format(n1, n2, rs))
    elif vc == 5:
        print('Finalizando ... ')
        sleep(2)
    else:
        print('Opção Inválida. Tente outra vez...')
    print('*-' * 10)



