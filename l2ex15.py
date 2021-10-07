'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem
 ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;'''
def valida(ret):
    if ret[0] + ret[1] > ret[2] and ret[0] + ret[2] > ret[1] and ret[1] + ret[2] > ret[0]:
        return True
    else:
        return False


def tipo(ret):
    if ret[0] == ret[1] and ret[1] == ret[2] and ret[0] == ret[2]:
        return "Equilátero"
    elif ret[0] == ret[1] or ret[1] == ret[2] or ret[0] == ret[2]:
        return "Isósceles"
    else:
        return "Escaleno"


retas = []

for i in range(0,3):
    r = float(input(f'Informe o lado da {i+1} reta: '))
    retas.append(r)

if valida(retas):
    print(f'Triângulo {tipo(retas)} formado')
else:
    print('As retas informadas não podem formar um triângulo.')