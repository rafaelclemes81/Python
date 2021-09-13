'''FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA maior(), QUE RECEBA VÁRIOS
PARÂMETROS COM VALORES INTEIROS. SEU PROGRAMA TEM QUE ANALISAR TODOS OS VALORES E DIZER
QUAL DELES É O MAIOR.'''
def maior(* num):
    cont = maior = 0
    print('Analisando os valores passados ... ')
    for valor in num:
        print(f'{valor}', end=' ')
        if valor > maior:
            maior = valor
        cont += 1
    print()
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    print('-=' * 50)


#Programa Principal
maior(2, 9, 5, 6, 10, 1, 7, 8, 100)
maior(5, 3, 0)
maior(1, 2)
maior(9)
maior()