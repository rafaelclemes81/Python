''' REFAÇA O EXERCICIO 009, MOSTRANDO A TABUADA DE NÚMERO ESCOLHIDO PELO USUÁRIO, SÓ QUE AGORA
UTILIZANDO O LAÇO FOR'''
n = int(input('Que tabuada você quer exibir: '))
for i in range(1, 11):
    print('{} x {} = {}'.format(n, i, (n * i)))
