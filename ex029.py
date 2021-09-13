"""escreva um programa que leia a velocidade de um carro.
	Se ele ultrapassar 80km/h, mostre uma msg dizendo que ele foi multado
	A multa vai custar R$ 7,00 por cada km acima do limite"""

v = float(input('Informe a velocidade do carro: '))
if v > 80:
    print('Você foi multado e você vai precisar pagar um multa de R$ {:.2f}'.format((v - 80) * 7))
print('Tenha um bom dia, dirija com segurança!!!')
