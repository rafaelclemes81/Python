''' FAÇA UM PROGRAMA QUE FAÇA A SOMA ENTRE TODOS OS NÚMEROS ÍMPARES
QUE SÃO MÚLTIPLOS DE TRÊS NO INTERVALO DE 1 A 500'''
s = 0
c = 0
for i in range (1, 501):
    if (i % 2) > 0:
        if (i % 3) == 0:
            s += i
            c = c + 1
print('A soma dos {} números ímpares, múltiplos de 3 no intervalo entre 1 e 500 é {:.1f}'.format(c, s))
