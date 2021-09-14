'''Faça um Programa que leia três números e mostre o maior deles.'''
for i in range(0,3):
    num = int(input('Informe um número: '))
    if i == 0:
        maior = num
    else:
        if num > maior:
            maior = num

print(f'O maior número informado foi {maior}')