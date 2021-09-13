'''DESAFIO 023 - FAÇA UM PROGRAMA QUE LEIA M NÚMERO DE 0 A 9999 E MOSTRE NA TELA CADA UM DOS DÍGITOS SEPARADOS
	EX.: DIGITE UM NÚMERO: 1834
		UNIDADE:  4
		DEZENA: 3
		CENTENA: 8
		MILHAR: 1
'''

"""num = int(input('Digite um número: '))
n = str(num)
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(n[3], n[2], n[1], n[0]))"""

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(u, d, c, m))
