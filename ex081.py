''' CRIE UM PROGRAMA QUE VAI LER VÁRIOS VALORES E COLOCAR EM UMA LISTA
DEPOIS DISSO MOSTRE:
A-QUANTOS NÚMEROS FORAM DIGITADOS
B-A LISTA DE VALORES ORDENADA EM ORDEM DECRESCENTE
C-SE O VALOR 5 FOI DIGITADO E ESTÁ OU NÃO NA LISTA'''
lista = list()
while True:
    lista.append(int(input('Informe um número: ')))
    while True:
        r = str(input('Deseja continuar [S/N] ?')).strip().upper()
        if r in 'SN':
            break
        else:
            r = str(input('Deseja continuar [S/N] ?')).strip().upper()
    if r == 'N':
        break
print(f'A lista possui {len(lista)} elementos...')
lista.sort(reverse=True)
print(f'Lista ordenada em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5, não está na lista...')
