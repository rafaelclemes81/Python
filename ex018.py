'''Faça um programa que leia um
ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

from math import sin, cos, tan, radians
a = float(input('Informe um ângulo: '))
print('O seno de {:.2f}º é {:.2f}.\nO Cosseno de {:.2f}º é {:.2f}.\nA tangente de {:.2f}º é {:.2f}'.format(a, sin(radians(a)), a, cos(radians(a)), a, tan(radians(a))))
