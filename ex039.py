"""039 - FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM A SUA IDADE:
	- SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR
	- SE É A HORA DE SE ALISTAR
	- SE JÁ PASSOU DO TEMPO DO ALISTAMENTO
	O PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTOU OU QUE PASSOU DO PRAZO."""
from datetime import date
print ('-' * 20, 'DESAFIO 039', '-' * 20)
sexo = str(input('Informe o sexo M/F: '))
nasc = int(input('Olá, informe seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
if sexo == 'M':
    if idade < 18:
        print('Olá, você ainda não tem idade para se alistar no serviço militar. Ainda faltam {} anos.'.format(18-idade))
    elif idade == 18:
        print('Olá. Seja bem vindo ao serviço militar. Vamos proceder com o alistamento.')
    elif idade > 18:
        print('Olá, o serviço militar é uma obrigação em nosso país. Você deveria ter nos procurado há {} anos. Cumpra seu dever.'.format(idade-18))
else:
    print('Obrigado, o serviço militar não é obrigatório para mulheres.')
