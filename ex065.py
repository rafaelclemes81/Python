'''CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS. NO FINAL DA EXECUÇÃO MOSTRE A MÉDIA ENTRE ELES,
O MAIOR E O MENOR VALOR INFORMADO. O PROGRAMA DEVE PERGUNTAR SE O USUÁRIO QUER OU NÃO CONTINUAR'''
r = 'S'
c = 0
soma = 0
maior = 0
menor = 999999999
while r == 'S':
    c += 1
    n = int(input('Informe um número: '))
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    r = str(input('Deseja informar mais um número? ').upper())
print('''Você digitou {} números.
A média entre eles é {}.
Dentre os números informados o maior é {}.
Dentre os números informados o menor é {}'''.format(c, (soma / c), maior, menor))
