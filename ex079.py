''' CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR VÁRIOS VALORES NÚMERICOS E CADASTRE-OS
EM UMA LISTA. CASO O NÚMERO JÁ EXISTA LÁ DENTRO, ELE NÃO PODERÁ SER ADICIONADO.
NO FINAL, SERÃO EXIBIDOS TODOS OS VALORES ÚNICOS ADICIONADOS EM ORDEM CRESCENTE'''
lista = list()
while True:
    n = int(input('Informe um número: '))
    if n in lista: #poderia utilizar: if n not in lista:
        print('O número digitado já foi informado na lista.')
    else:
        lista.append(n)
        print('Número adicionado comsucesso ... ')
    while True:
        r = str(input('Deseja continuar [S/N] ?')).strip().upper()
        if r in 'SN':
            break
    if r == 'N':
        break
lista.sort()
print(f'A lista informado foi {lista}')

