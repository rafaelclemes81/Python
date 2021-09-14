'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.'''

nota = list()
soma = 0
for i in range(1, 3):
    nota.append(float(input(f'Informe a {i}ª nota: ')))

for i, n in enumerate(nota):
    soma += n
    print(f'Nota {i} - {n}')

media = soma / len(nota)

if media == 10:
    print(f'O aluno foi aprovado com excelência com {media:.2f}.')
elif media >= 7:
    print(f'O aluno foi aprovado com média {media:.2f}')
else:
    print(f'O aluno foi reprovado com média {media:.2f}')
