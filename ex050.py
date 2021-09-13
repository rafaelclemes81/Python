''' DESENVOLVA UM PROGRAMA QUE LEIA 6 NÚMEROS INTEIROS E MOSTRE A SOMA APENAS
DAQUELES QUE FOREM PARES. SE O VALOR INFORMADO FOR ÍMPAR DESCONSIDERE'''
s = 0
for i in range(1, 7):
    n = int(input('Informe um número inteiro: '))
    if (n % 2) == 0:
        s += n
print('A soma dos números pares dentre os informados é {}'.format(s))