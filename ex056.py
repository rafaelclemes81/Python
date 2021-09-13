''' DESENVOLVA UM PROGRAMA QUE LEIA O NOME, A IDADE E SEXO DE 4 PESSOAS.
NO FINAL DO PROGRAMA MOSTRE:
- A MÉDIA DE IDADE DO GRUPO
- QUAL É O NOME DO HOMEM MAIS VELHO
- QUANTAS MULHERES TEM MENOS DE 20 ANOS'''
soma = 0
qtmul = 0
velho = 0
for i in range(1,5):
    nome = str(input('Informe o nome da {}ª pessoa: '.format(i)))
    idade = int(input('Informa a idade da {}ª pessoa: '.format(i)))
    sexo = str(input('Informe o gênero da {}ª pessoa: '.format(i)))
    if idade > velho:
        nmvelho = nome
        velho = idade
    if sexo == 'F' or sexo == 'f' and idade < 20:
        qtmul = qtmul + 1
    soma = soma + idade
print('''A média das idades informadas é {}
O nome do homem mais velho é {}
{} mulheres possuem menos de 20 anos'''.format((soma / 4), nmvelho, qtmul))
