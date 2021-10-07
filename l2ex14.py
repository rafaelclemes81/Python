'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito
for A, B ou C ou “REPROVADO” se o conceito for D ou E.'''
import os

def cabecalho(c, t):
    print(f'-' * t)
    print(f'{c:^{t}}')
    print(f'-' * t)


def resultado (r, t, nts):
    soma = 0
    print(f'-' * t)
    print(f'{r:^{t}}')
    print(f'-' * t)
    for i in range(0, 2):
        soma += nts[i]
    media = soma / len(nts)
    for i, v in enumerate(nts):
        print(f'NOTA {i+1}: {v:.2f}')
    print(f'Média Final: {media:.2f}')
    if 9 <= media <= 10:
        print(f'Conceito: A'
              f'\nSituação: Aprovado')
    elif 7.5 <= media < 9:
        print(f'Conceito: B'
              f'\nSituação: Aprovado')
    elif 6 <= media < 7.5:
        print(f'Conceito: C'
              f'\nSituação: Aprovado')
    elif 4 <= media < 6:
        print(f'Conceito: D'
              f'\nSituação: Reprovado')
    else:
        print(f'Conceito: E'
              f'\nSituação: Reprovado')


notas = []
cabecalho('COLETA DE NOTAS', 30)
for i in range(0,2):
    notas.append(float(input(f'Informe a {i+1}ª nota: ')))
resultado('Resultado Final', 30, notas)


