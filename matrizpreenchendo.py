turma = []
for i in range(1):
    linha = []
    for j in range(5):
        linha.append(float(input(f'Informe a {j+1}ª nota do {i+1}º aluno: ')))
    turma.append(linha)

soma = 0
#calculando a média dos alunos
for i in range(3):
    for j in range(5):
        soma += linha[j]
        media = soma / (j+1)
        #imprimir dados dos alunos
        print(f'Aluno {j+1} - Notas: {linha[j]} - Média {media}')

