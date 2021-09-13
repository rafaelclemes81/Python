''' CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCAR EM UMA LISTA.
DEPOIS DISSO, CRIE DUAS LISTA EXTRAS QUE VÃO CONTER APENAS OS VALORES PARES E OS VALORES
ÍMPARES DIGITADOS, RESPECTIVAMENTE. AO FINAL MOSTRE OS VALORES DAS 3 LISTAS'''
lista = list()
pares = list()
impares = list()
while True:
    n = int(input('Informe um número: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    while True:
        r = str(input('Deseja continuar [S/N] ?')).strip().upper()[0]
        if r in 'SN':
            break
        else:
            r = str(input('Deseja continuar [S/N] ?')).strip().upper()[0]
    if r == 'N':
        break
print(f'Lista completa: {lista}')
print(f'Lista de pares: {pares}')
print(f'Lista de ímpares: {impares}')

