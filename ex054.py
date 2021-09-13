''' CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS. NO FINAL, MOSTRE QUANTAS PESSOAS
AINDA NÃO ATINGIRAM A MAIORIDADE E QUANTAS JÁ SÃO MAIORES'''
from datetime import datetime
menores = 0
maiores = 0
for i in range(1,8):
    ano = int(input('Informe o ano de nascimento da {}ª pessoa: '.format(i)))
    if (datetime.today().year - ano) < 21:
        menores += 1
    else:
        maiores += 1
print('Das sete pessoas, {} são menores de idade e {} já atingiram a maioridade.'.format(menores, maiores))