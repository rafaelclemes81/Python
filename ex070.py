''' CRIE UM PROGRAMA QUE LEIA NOME E PREÇO DE VÁRIOS PRODUTOS.
O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO VAI CONTINUAR. NO FINAL MOSTRE:
A - QUAL É O TOTAL GASTO NA COMPRA
B - QUANTOS PRODUTOS CUSTAM MAIS DE R$ 1000,00
C - QUAL O NOME DO PRODUTO MAIS BARATO'''
compra = 0
caros = 0
caro = 0
barato = 999999999
resp = 'S'
while resp == 'S':
    produto = str(input('Informe a descrição do produto: ').strip().upper())
    preco = float(input('Informe o preço do produto: '))
    compra += preco
    if preco > caro:
        caros += 1
        caro = preco
    if preco < barato:
        nome = produto
        barato = preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? ').strip().upper())[0]
print(f'''O total da compra foi de {compra:.2f}
{caros} produtos custaram mais de R$ 1000,00
O produto mais barato informado foi: {nome}''')