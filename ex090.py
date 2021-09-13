'''FAÇA UM PROGRAMA QUE LEIA O NOME E A MÉDIA DE UM ALUNO, GUARDANDO TAMBÉM A SITUAÇÃO
EM UM DICIONÁRIO. NO FINAL MOSTRE O CONTEÚDO DA ESTRUTURA NA TELA.'''
aluno = {}
aluno['Nome'] = str(input('Informe o nome do aluno: '))
aluno['Média'] = float(input(f'Informe a média de {aluno["Nome"]}: '))
if aluno['Média'] > 6.9:
    aluno['situação'] = 'Aprovado'
elif aluno['Média'] > 4.9:
    aluno['situação'] = 'em recuperação'
else:
    aluno['situação'] = 'reprovado'
for k, v in aluno.items():
    print(f'{k} é {v}')

