''' CRIE UM PROGRAMA ONDE O USUÁRIO DIGITE UMA EXPRESSÃO QUALQUER QUE USE PARENTESES.
SEU APLICATIVO DEVERÁ ANALISAR SE A EXPRESSÃO PASSADA ESTÁ COM OS PARENTESES ABERTOS
E FECHADOS NA ORDEM CORRETA'''
exp = str(input('Digite a expressão: '))
pilha = list()
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida...')
else:
    print('Sua expressão está incorreta ... ')