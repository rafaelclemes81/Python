''' faça um programa que tenha uma função notas() que pode receber
várias notas de alunso e vai retornar um dicionário com as seguintes
informações:
- quantidade de notas
- a maior nota
- a menor nota
- a média da turma
- a situação(opcional)

adicione também as docstrings da função'''
def notas(*n, sit=False):
    """
    --> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indica se deve ou não adicionar a situação do aluno
    :return: dicionário com total de notas, a maior nota, a menor nota, a média entre as notas e,
             em caso de sit=True, a situação do aluno
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        elif r['media'] >= 4:
            r['situacao'] = 'RUIM'
        else:
            r['situacao'] = 'DESISTE'
    return r

# Programa Principal
resp = notas(5.5, 4.5, 2.8, 1.5, sit=True)
print(resp)
help(notas)