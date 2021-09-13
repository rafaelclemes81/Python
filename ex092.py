'''CRIE UM PROGRAMA QUE LEIA NOME, ANO DE NASCIMENTO E CARTEIRA DE TRABALHO E CADASTRE-OS
(CALCULANDO A IDADE) EM UM DICIONÁRIO. SE POR ACASO A CTPS FOR DIFERENTE DE ZERO, O DICIONÁRIO
RECEBERÁ TAMBÉM O ANO DE CONTRATAÇÃO E O SALÁRIO. CALCULE E ACRESCENTE, ALÉM DA IDADE, COM QUANTO
ANOS A PESSOA VAI SE APOSENTAR(35 ANOS DE CONTRIBUIÇÃO)'''
from datetime import datetime
trabalhador = {}
trabalhador['Nome'] = str(input('Informe o nome: '))
trabalhador['Idade'] = datetime.today().year - int(input('Informe o ano de nascimento: '))
trabalhador['CTPS'] = int(input('Informe o número da CTPS (0 quando não tiver): '))
if trabalhador['CTPS'] > 0:
    trabalhador['Admissão'] = int(input('Informe o ano da admissão: '))
    trabalhador['Salário'] = float(input('Informe o salário: '))
    trabalhador['Tempo de Serviço'] = datetime.today().year - trabalhador['Admissão']
    trabalhador['Idade Aposentadoria'] = trabalhador['Idade'] + (35 - trabalhador['Tempo de Serviço'])
print('-' * 40)
for k, v in trabalhador.items():
    print(f'{k}: {v}')