'''Faça um programa que pergunte o preço de três produtos e informe
qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''
for i in range(0,3):
    preco = float(input(f'Informe o preço do {i+1}º produto: '))
    if i == 0:
        menor = preco
    elif preco < menor:
        menor = preco
print(f'O menor preço informado foi {menor:.2f}')