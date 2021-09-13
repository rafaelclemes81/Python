'''FAÇA UM PROGRAMA QUE LEIA 5 VALORES NÚMEROS E GUARDE-OS EM UMA LISTA.
NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR VALOR DIGITADO E AS SUAS RESPECTIVAS POSIÇÕES NA LISTA'''
print('=.' * 12)
lista = list()
for i in range(0,5):
    lista.append(int(input(f'Informe o {i+1}º número: ')))
    if i == 0:
        menor = maior = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
print('=.' * 12)
print(f'A lista digitada foi: {lista}')
print(f'O maior número digitado foi {maior} na(s) posição(ões) ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i+1}...')
print(f'O menor número digitado foi {menor} na(s) posição(ões)', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i+1}...')
print('Fim do programa ... ')