'''Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.'''
dia = int(input('Informe um número entre 1 e 7: '))
if dia == 1:
    print(f'O {dia}º dia da semana é domingo.')
elif dia == 2:
    print(f'O {dia}º dia da semana é segunda-feira.')
elif dia == 3:
    print(f'O {dia}º dia da semana é terça-feira.')
elif dia == 4:
    print(f'O {dia}º dia da semana é quarta-feira.')
elif dia == 5:
    print(f'O {dia}º dia da semana é quinta-feira.')
elif dia == 6:
    print(f'O {dia}º dia da semana é sexta-feira.')
elif dia == 7:
    print(f'O {dia}º dia da semana é sábado.')
else:
    print('O número informado não corresponde a nenhum dia da semana.')
