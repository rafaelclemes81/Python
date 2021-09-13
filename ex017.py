'''Faça um programa que leia o comprimento do cateto oposto e do
cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''

from math import hypot
y = float(input('Informa o cateto oposto do triângulo: '))
x = float(input('Informe o catelo adjacente do triangulo: '))
print ('A hipotenusa do triângulo é {:.2f}'.format(hypot(x,y)))