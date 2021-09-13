''' CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. O PROGRAMA SÓ
VAI PARAR QUANDO O USUÁRIO DIGITAR A FLAG 999. NO FINAL MOSTRAR QUANTOS NÚMEROS FORAM DIGITADOS
E A SOMA ENTRE ELES DESCONSIDERANDO A FLAG'''
c = 0
soma = 0
while True:
    n = int(input('Informe um número [999 para encerrar]: '))
    if n == 999:
        break
    c += 1
    soma += n
print(f'Foram digitados {c}. A soma total dos números informados foi {soma}')
