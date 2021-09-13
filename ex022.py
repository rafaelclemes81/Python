'''CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
	O NOME COM TODAS AS LETRAS MAÍSCULAS
	O NOME COM TODAS AS LETRAS MINÚSCULAS
	QUANTAS LETRAS AO TODO SEM CONSIDERAR OS ESPAÇOS
	QUANTAS LETRAS TEM O PRIMEIRO NOME'''
nome = str(input('Informe seu nome completo: ')).strip()
print('Nome convertido em maiúsculo: {}'.format(nome.upper()))
print('Nome convertido em minúsculo: {}'.format(nome.lower()))
print('O nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
div = nome.split()
print('O primeiro nome é {} e possui {} letras'.format(div[0], len(div[0])))
