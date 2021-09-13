"""041 - A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA
      E MOSTRE SUA CATEGORIA, DE ACORDO COM A IDADE:
	- ATÉ 9 ANOS: MIRIM
	- ATÉ 14 ANOS: INFANTIL
	- ATÉ 19 ANOS: JUNIOR
	- ATÉ 20 ANOS: SÊNIOR
	- ACIMA: MASTER"""
from datetime import date
print('-' * 20, 'DESAFIO 041', '-' * 20)
nasc = int(input('Informe o ano do nascimento do atleta: '))
atual = date.today().year
idade = atual - nasc
if idade <= 9:
    print('O atleta informado possui {} anos e sua categoria é MIRIM.'.format(idade))
elif idade <= 14:
    print('O atleta informado possui {} anos e sua categoria é INFANTIL.'.format(idade))
elif idade <= 19:
    print('O atleta informado possui {} anos e sua categoria é JUNIOR.'.format(idade))
elif idade <= 25:
    print('O atleta informado possui {} anos e sua categoria é SÊNIOR.'.format(idade))
else:
    print('O atleta informado possui {} anos e sua categoria é MASTER.'.format(idade))
