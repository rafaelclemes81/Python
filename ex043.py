"""043 - DESENVOLVA UMA LÓGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA, CALCULO SEU IMC E MOSTRE SEU STATUS,
      DE ACORDO COM A TABELA ABAIXO:
	- ABAIXO DE 18,5: ABAIXO DO PESO
	- ENTRE 18,5 E 25: PESO IDEAL
	- ENTRE 25 E 30: SOBREPESO
	- ENTRE 30 E 40: OBESIDADE MORBIDA"""
print('-' * 20, 'DESAFIO 043', '-' * 20)
p = float(input('Informe seu peso:   '))
a = float(input('Informe sua altura: '))
imc = p / (a ** 2)
if imc < 18.5:
    print('Seu IMC é de {:.2f}kg/m e você está abaixo do peso.'.format(imc))
elif imc <= 25:
    print('Seu IMC é de {:.2f}kg/m e você está no peso ideal.'.format(imc))
elif imc <= 30:
    print('Seu IMC é de {:.2f}kg/m e você está com sobrepeso.'.format(imc))
else:
    print('Seu IMC é {:.2f}kg/m e você está com obesidade morbida.'.format(imc))

