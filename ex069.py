''' CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VÁRIAS PESSOAS. A CADA PESSOA CADASTRADA, O PROGRAMA
DEVERÁ PERGUNTAR SE O USUÁRIO QUER OU NÃO CONTINUAR. NO FINAL MOSTRE:
A - QUANTAS PESSOAS TEM MAIS DE 18 ANOS
B - QUANTOS HOMENS FORAM CADASTRADOS
C - QUANTAS MULHERES TEM MENOS DE 20 ANOS'''
maiores = 0
homens = 0
mulheres = 0
resp = 'S'
genero = ' '
while resp == 'S':
    idade = int(input('Informe a idade: '))
    while genero not in 'MF':
        genero = str(input('Informe o gênero: ').strip().upper())[0]
    if idade > 18:
        maiores += 1
    if genero == 'M':
        homens += 1
    else:
        if idade < 20:
            mulheres += 1
    resp = ' '
    genero = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar ?').strip().upper())[0]
print(f'''{maiores} pessoas são maiores de 18 anos.
{homens} homens foram informados.
{mulheres} mulheres com menos de 20 anos foram informadas.''')
