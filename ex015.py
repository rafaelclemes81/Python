#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
#  ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Quantos quilometros foram percorridos? '))
d = int(input('Por quantos dias o carro ficou alugado ?'))
print('Você alugou o carro por {} dias e percorreu {:.2f} kilometros.O valor total a pagar é de {:.2f}'.format(d, km, (d*60)+(km*0.15)))