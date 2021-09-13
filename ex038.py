"""038 - ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E COMPARE-OS:
	MOSTRANDO NA TELA UMA MENSAGEM:
	- O PRIMEIRO VALOR É MAIOR
	- O SEGUNDO VALOR É MAIOR
	- NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS"""
print('*' * 10, ' DESAFIO 038 ', '*' * 10)
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número : '))
if n1 > n2:
   print('O primeiro número informado {} é o maior.'.format(n1))
elif n2 > n1:
   print('O segundo número informado {} é o maior.'.format(n2))
else:
   print('Não existe número maior, ambos são iguais.')