''' CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS, O PROGRAMA SÓ VAI PARAR QUANDO FOR
INFORMADO O NÚMERO 999, QUE É A CONDIÇÃO DE PARADA. NO FINAL MOSTRE QUANTOS NÚMEROS FORAM INFORMADOS
E A SOMA DELES, DESCONSIDERANDO A FLAG'''
c = 0
soma = 0
n = int(input('Informe um número [999 para finalizar]: '))
while n != 999:
    c += 1
    soma += n
    n = int(input('Informe um número [999 para finalizar]: '))
print('Você digitou {} números e a soma deles é {}.'.format(c, soma))
