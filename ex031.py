"""desenvolva que pergunte a distância de uma viagem em km.
	Calcule o valor da passagem, cobrando R$ 0,50/km para viagens até 200km
	e R$ 0,45/km para viagens maiores que 200 km *** duas formas de fazer ***"""

d = float(input('Olá, qual a distãncia da sua viagem? '))
"""if d > 200:
    print('O valor da sua passagem é {}'.format(d * 0.45))
else:
    print('O valor da sua passagem é {}'.format(d * 0.50))""" #PRIMEIRA FORMA DE RESOLVER

preco = d * 0.45 if d > 200 else d * 0.50 #SEGUNDA FORMA DE RESOLVER
print('O valor da sua passagem de {} km(s) será de R${}. Tenha uma ótima viagem!!!'.format(d, preco))


