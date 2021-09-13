"""042 - REFAÇA O DESAFIO 035 DOS TRIÂNGULOS, ACRESCENTANDO O RECURSO DE MOSTRAR QUE TIPO DE TRIÂNGULO SERÁ FORMADO:
    - EQUILÁTERO: TODOS OS LADOS IGUAIS
    - ISÓSCELES: DOIS LADOS IGUAIS
    - ESCALENO: TODOS OS LADOS DIFERENTES"""
print('-' * 20, 'DESAFIO 042', '-' * 20)
a = int(input("Informe o tamanho da reta 1 em CM: "))
b = int(input('Informe o tamanho da reta 2 em CM: '))
c = int(input('Informe o tamanho da reta 3 em CM: '))
if (((b - c) < a) and (a < (b + c))) and (((a - c) < b) and (b < (a + c))) and (((a - b) < c) and (c < (a + b))):
    if a == b and b == c:
        print('Triângulo equilátero formado.')
    elif a == b or a == c or b == c:
        print('Triângulo isóceles formado.')
    elif a != b and b != c:
        print('Triângulo escaleno formado.')
else:
    print('As retas informadas não podem formar um triângulo.')
