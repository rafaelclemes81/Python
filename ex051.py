'''DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PROGRESSÃO ARITMÉTICA. NO FINAL
MOSTRE OS 10 PRIMEIROS TERMOS DESTA PROGRESSÃO'''
n = int(input('Informe um número: '))
r = int(input('Informe a razão para a P.A.: '))
print('O 1º número da PA é {}'.format(n))
for i in range(2, 11):
    n += r
    print('O {}º número da PA é {}'.format(i, n))