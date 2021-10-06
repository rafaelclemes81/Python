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


def cabecalho(c, t):
    print(f'-' * t)
    print(f'{c:^{t}}')
    print(f'-' * t)


def resultado(n, m):
    for i, v in enumerate(n):
        print(f'Nota{v}: ')


notas = []
soma = 0
cabecalho('COLETA DE NOTAS', 30)
for i in range(0,2):
    notas.append(float(input(f'Informe a {i+1}ª nota: ')))

for i in range(0,2):
    soma += notas[i]

media = soma / len(notas)

if 9<= media <=10:
    cabecalho('Resultado do Aluno', 30)

