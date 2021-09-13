''' CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRÔNICO
NO INÍCIO VAI PERGUNTAR AO USUÁRIO O VALOR A SER SACADO (NÚMERO INTEIRO) E O PROGRAMA VAI INFORMAR
QUANTAS CÉDULAS DE CADA VALOR SERÃO ENTREGUES, CONSIDERANDO QUE O CAIXA POSSUI CÉDULAS DE 50, 20
10 E 1 REAL'''
print('=' * 30)
print('{:^30}'.format('BANCO RAFAEL'))
print('=' * 30)
valor = int(input('Qual o valor do saque ? R$ '))
total = valor
cedula = 50
totced = 0
while True:
    if total >= cedula:
        total -= cedula
        totced += 1
    else:
        if totced > 0:
            print(f'Total de cédula de {cedula}: {totced}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao Banco Rafael')