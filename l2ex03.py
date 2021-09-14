'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
 F - Feminino, M - Masculino, Sexo Inválido.'''

genero = str(input('Informe o gênero [F/M]: ')).strip().upper()
if genero not in 'FM':
    print(f'Sexo Inválido')
else:
    if genero == 'M':
        print('M - Masculino')
    else:
        print('F - Feminino')



