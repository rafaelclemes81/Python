'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''
for i in range(0,3):
    num = int(input(f'Informe o {i}º número: '))
    if i == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
print(f'O menor número informado foi {menor} e o maior número informado foi {maior}')