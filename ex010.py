#CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR / COTAÇÃO DO DÓLAR = R$ 3,27
c = float(input('Quanto R$ você tem para compras doláres? '))
print('Com R$ {:.2f} você poderá compras USD {:.2f} e EUR {:.2f}'.format(c, c/3.27, c/5.54))