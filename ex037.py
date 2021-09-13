"""037 - ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USUÁRIO ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO:
	1 - BINÁRIO
	2 - OCTAL
	3 - HEXADECIMAL"""
print('-*-' * 10, 'CONVERSOR', '-*-' * 10)
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
n = int(input('Informe o número a ser convertido: '))
b = int(input('Informe a base de conversão: '))
if b == 1:
	print('O número {} convertido para binário é {}'.format(n,bin(n)))
elif b == 2:
	print('O número {} convertido para octal é {}'.format(n,oct(n)))
elif b == 3:
	print('O número {} convertido para hexadecimal é {}'.format(n,hex(n)))
else:
    print('A base informada não foi encontrada')