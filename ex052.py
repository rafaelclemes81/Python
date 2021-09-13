'''FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU NÃO PRIMO'''
tot = 0
n = int(input('Informe um número inteiro: '))
for i in range(1, n+1):
    if n % i == 0:
        print('\033[34m', end='')
        tot = tot + 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO número {} foi divisível por {} vezes'.format(n, tot), end='')
if tot == 2:
    print('\nPor isso o número {} é primo'.format(n))
else:
    print('\nPor isso o número {} é NÃO é primo'.format(n))
