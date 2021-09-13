'''FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESSIVA
PARA O ESTOURO DE FOGOS DE ARTIFÍCIOS, INDO DE 10 ATÉ 0, FAZENDO UMA PAUSA DE 1 SEGUNDO
ENTRE ELES'''
from time import sleep
for i in range(10, 0, -1):
    print(i)
    sleep(1)
print('Feliz ano novo!!!')
