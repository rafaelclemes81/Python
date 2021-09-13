'''FAÇA UM PROGRAMA QUE TENHA UMA LISTA CHAMADA 'NÚMEROS' E DUAS FUNÇÕES CHAMADAS SORTEIA()
E SOMAPAR(). A PRIMEIRA FUNÇÃO VAI SORTEAR 5 NÚMEROS E VAI COLOCÁ-LOS DENTRO DA LISTA. A SEGUNDA
VAI MOSTRAR A SOMA ENTRE TODOS OS VALORES PARES, SORTEADOS PELA FUNÇÃO ANTERIOR.'''
from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores para a lista: ', end='')
    for v in range(0, 5):
        lista.append(randint(0, 100))
        print(f'{lista[v]} ', end='')
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista} temos {soma}')


#Programa Principal
numeros = list()
sorteia(numeros)
somaPar(numeros)
