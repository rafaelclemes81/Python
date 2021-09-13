''' FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VÁRIOS NÚMEROS, UM DE CADA VEZ, PARA CADA VALOR
DIGITADO PELO USUÁRIO. O PROGRAMA SERÁ INTERROMPIDO QUANDO FOR INFORMADO UM VALOR NEGATIVO'''
while True:
    print('=-' * 20)
    n = int(input('Informe um número: '))
    if n < 0:
        break
    for i in range (1,11):
        print(f'{n} x {i} = {n * i}')
print('Programa encerrado. Até breve')