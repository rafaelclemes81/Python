#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input('Informe a temperatura em Cº: '))
print('{:.1f}ºC equivalem a {:.1f}ºF'.format(celsius, celsius*1.8+32))
