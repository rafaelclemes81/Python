#FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA
#E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA, PINTA UMA ÁREA DE 2 M2
l = float(input('Informa a altura da parede: '))
a = float(input('Informa a altura da parede: '))
print('A sua parece tem {:.2f} X {:.2f}m e a área total é de {:.2f}m2. Para pintá-la você irá precisar de {:.2f} litros de tinta'.format(l, a, l*a, l*a/2))