''' FAÇA~UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SÓ ACEITE OS VALORES 'M' OU 'F'
CASO ESTEJA INFORMADO DE OUTRA FORMA, PEÇA A DIGITAÇÃO NOVAMENTE ATÉ RECEBER UM VALOR CORRETO'''
s = 'A'
while s not in 'MF':
    s = str(input('Informe o gênero: ').upper().strip())[0]
print('Sexo Informado {}'.format(s))