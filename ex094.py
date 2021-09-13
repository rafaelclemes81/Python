''' CRIE UM PROGRAMA QUE LEIA NOME, SEXO E IDADE DE VÁRIAS PESSOAS, GUARDANDO OS DADOS
DE CADA PESSOA EM UM DICIONÁRIOS, E TODOS OS DICIONÁRIOS EM UMA LISTA.
NO FINAL MOSTRE:
A-QUANTAS PESSOAS FORAM CADASTRADAS
B-A MÉDIA DE IDADE DO GRUPO
C-UMA LISTA COM TODAS AS MULHERES
D-UMA LISTA COM TODAS AS PESSOAS COM IDADE ACIMA DA MÉDIA'''
lista = list()
pessoa = dict()
soma = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['gênero'] = str(input('Gênero: [M/F] ')).strip().upper()[0]
        if pessoa['gênero'] in 'MF':
            break
        print('Erro, por favor digite M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    lista.append(pessoa.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro. Informe S ou N.')
    if resp == 'N':
        break
print(f'Ao todo foram cadastradas {len(lista)} pessoas.')
print(f'A média das pessoas cadastradas é de {(soma / len(lista)):5.2f} anos')
print('As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['gênero'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('As pessoas que possuem idade acima da média são: ')
for p in lista:
    if p['idade'] > (soma / len(lista)):
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
        print()
print('<<< ENCERRADO >>>')
