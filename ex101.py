''' CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMDA VOTO() QUE VAI RECEBER
COMO PARÂMETRO O ANO DE NASCIMENTO DE UMA PESSOA, RETORNANDO UM VALOR
LITERAL INDICANDO SE UMA PESSOA TEM VOTO NEGADO, OPCIONAL OU OBRIGATÓRIO NAS
ELEIÇÕES.'''
from datetime import datetime
def voto(a=1900):
    global atual
    atual = datetime.today().year
    if 65 > atual - a >= 18:
        return 'OBRIGATORIO'
    elif atual - a >= 65:
        return 'OPCIONAL'
    elif atual - a >= 16:
        return 'OPCIONAL'
    else:
        return 'VOCÊ AINDA NÃO PODE VOTAR.'


# Programa principal
ano = int(input('Informe o ano de seu nascimento: '))
idade = datetime.today().year - ano
print(f'Seu ano de nascimento é {ano}. Com {idade} anos o voto é {voto(ano)}')
