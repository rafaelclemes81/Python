''' CRIE UM PROGRAMA QUE TENHA UMA TUPLA TOTALMENTE PREENCHUIDA COM UMA CONTAGEM POR EXTENSO, DE ZERO ATÉ VINTE.
SEU PROGRAMA DEVERÁ LER UM NÚMERO PELO TECLADO(ENTRE 0 E 20) E MOSTRÁ-LO POR EXTENSO'''
extenso = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número: '))
    if 0<= n <= 20:
        break
    print('Tente novamente... ', end='')
print(f'O número digitado foi {extenso[n]}')
print('Fim do programa...')