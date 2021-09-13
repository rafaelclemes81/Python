"""desenvolva um programa que leia o tamanho de 3 retas e diga se elas podem ou não formar um triângulo"""
a = int(input("Informe o tamanho da reta 1 em CM: "))
b = int(input('Informe o tamanho da reta 2 em CM: '))
c = int(input('Informe o tamanho da reta 3 em CM: '))
if (((b - c) < a) and (a < (b + c))) and (((a - c) < b) and (b < (a + c))) and (((a - b) < c) and (c < (a + b))):
	print('Triângulo formado.')
else:
	print('As retas informadas não podem formar um triângulo.')
