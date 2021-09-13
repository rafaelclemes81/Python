"""escreva um programa que pergunte o salário de funcionário e calcule o valor do aumento
	para salários superiores a R$ 1250,00, 10% de aumento
	para salários menores ou iguais a R$ 1250,00, aumento de 15%"""
s = float(input('Informe o salário: '))
if s > 1250:
    s = s * (10/100+1)
else:
    s = s * (15/100+1)
print('Seu salário foi reajustado para {} '.format(s))
