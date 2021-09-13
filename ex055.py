''' FAÇA UM PROGRAMA QUE LEIA O PESO DE 5 PESSOAS. NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR PESO LIDOS'''
maior = 0
menor = 9999
for i in range(1, 6):
    peso = float(input('Informe o peso da {}ª pessoa: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('A pessoa mais pesada possui {} kilos e a mais leve pesa {} kilos.'.format(maior, menor))