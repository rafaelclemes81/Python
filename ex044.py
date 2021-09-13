"""044 - ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO, CONSIDERANDO O SEU PREÇO NORMAL
      E CONDIÇÃO DE PAGAMENTO:
	1- À VISTA DINHEIRO/CHEQUE: 10% DE DESCONTO
	2- À VISTA NO CARTÃO: 5% DE DESCONTO
	3- EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
	4- EM 3X OU MAIS NO CARTÃO: 20% DE JUROS"""
print('{:=^40}'.format(' DESAFIO 44 '))
p = float(input('Informe o valor do produto:  '))
print('''1 - À VISTA DINHEIRO/CHEQUE: 10% DE DESCONTO
2 - À VISTA NO CARTÃO: 5% DE DESCONTO
3 - EM ATÉ 2X NO CARTÃO.PREÇO NORMAL
4 - EM 3X OU MAIS NO CARTÃO: 20% DE JUROS''')
c = int(input('Escolha uma codição de pagamento: '))
if c == 1:
    print('Você ganhou 10% de desconto. Seu produto vai custar R${:.2f}.'.format(p * (1-(10/100))))
elif c == 2:
    print('Você ganhou 5% de desconto. Seu produto vai custar R${:.2f}.'.format(p * (1 - (5 / 100))))
elif c == 3:
    print('Você parcelou em 2x no cartão sem juros. Seu produto vai custar R${:.2f}.'.format(p))
elif c == 4:
    print('Nessas condições o produto terá 20% de juros. Seu produto vai custar R${:.2f}'.format(p * (1+(20/100))))
else:
    print('Escolha uma condição de pagamento VÁLIDA')
