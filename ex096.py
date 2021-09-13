''' FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA 'ÁREA', QUE RECEBA AS DIMENSÕES
DE UM TERRENO RETANGULAR (LARGURA E COMPRIMENTO) E MOSTRE A ÁREA DO TERRENO'''
def cabecalho(titulo):
    print('=-' * 50)
    print(f'{titulo:^100}')
    print('=-' * 50)

def areaterreno(larg, comp):
    areatotal = larg * comp
    print(f'A área total do terreno com as dimensões de {larg:.2f} x {comp:.2f} é de {areatotal:.2f} m2')


#Programa Principal
cabecalho('CÁLCULO DE ÁREA DE TERRENO')
l = float(input('Informa a largura do terreno: '))
c = float(input('Informe o comprimento do terreno: '))
areaterreno(l, c)
