''' FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA contador(), QUE RECEBA 3 PARÂMETROS
(INÍCIO, FIM E PASSO) E REALIZE A CONTAGEM.

SEU PROGRAMA TEM QUE REALIZAR 3 CONTAGENS ATRÁVES DA FUNÇÃO CRIADA.
A) DE 0 A 10, PASSO 1
B) DE 10 A 0, PASSO -2
C) UMA CONTAGEM PERSONALIZADA

obs.: ver no vídeo da aula 19 o que fazer'''
from time import sleep
def contar(a, b, p):
    print(f'Contagem de {a} até {b} de {p} em {p}')
    sleep(2.5)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    cont = a
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('Fim')
    else:
        cont = a
        while cont >= b:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('Fim')

def cabecalho(titulo):
    print('=-' * 50)
    print(f'{titulo:^100}')
    print('=-' * 50)

#Programa Principal
cabecalho('CONTADOR')
contar(0, 10, 1)
contar(10, 0, 2)
a = int(input('Informe o início da contagem: '))
b = int(input('Informe o final da contagem: '))
c = int(input('Informe o passo da contagem: '))
contar(a, b, c)
