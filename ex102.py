''' crie um programa que tenha uma função fatorial() que receba
dois parâmetros: o primeiro que indique o número a calcular e o outro
chamdo show que será um valor lógico(opcional) indicando se será mostrado ou não na tela
o processo de cálculo do fatorial. *** INCLUIR DOCSTRING NA FUNÇÃO '''
def fatorial(n, s=False):
    """
    Essa função calcula o fatorial de um número inteiro. É opcional detalhar a exibição do cálculo.
    :param n: Recebe o número do qual se deseja obter o fatorial
    :param s: Recebe um valor lógico. Caso seja True, será mostrado o cálculo do fatorial
    :return: n
    """
    if not s:
        fat = n
        for i in range (1, n):
            fat = (fat * (n-i))
        print(f'Fatorial de {n} é {fat}.')
    else:
        fat = n
        print(f'Cálculo detalhado do fatorial de [{n}] = {n} x ', end='')
        for i in range(1, n):
            fat = (fat * (n - i))
            if i == n-1:
                print(f'{n - i} = ', end='')
            else:
                print(f'{n - i} x ', end='')
        print(fat)



# Programa Principal
fatorial(5, s=True)
print(help(fatorial))
