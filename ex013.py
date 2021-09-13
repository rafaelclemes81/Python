#FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO, COM 15% DE AUMENTO
s = float(input('Informe seu salário: '))
print('Seu salário com 15% de reajuste será de R$ {:.2f}'.format(s+(s*15/100)))
