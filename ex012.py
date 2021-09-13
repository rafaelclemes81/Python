#FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO
preco = float(input('Informe o valor do produto: R$'))
print('O valor do produto com 5% de desconto é R$ {:.2f}'.format(preco-(preco*5/100)))
