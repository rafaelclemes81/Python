'''CRIE UM PROGRAMA QUE GERENCIE O APROVEITAMENTO DE UM JOGADOR DE FUTEBOL.
O PROGRAMA VAI LER O NOME DO JOGADOR E QUANTAS PARTIDAS ELE JOGOU. DEPOIS VAI LER A QUANTIDADE DE GOLS
FEITOS EM CADA PARTIDA. AO FINAL, TUDO ISSO SERÁ GUARDADO EM UM DICIONÁRIO, INCLUINDO O TOTAL
DE GOLS FEITOS DURANTE O CAMPEONATO'''
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for i in range (0, tot):
        partidas.append(int(input(f'   Quantos gols {jogador["nome"]} fez na partida {i+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro. Informe S ou N.')
    if resp == 'N':
        break
print('-' * 44)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:^15}', end='')
print()
print('-' * 44)
for k,v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):^15}', end='')
    print()
print('-' * 44)
while True:
    busca = int(input('Mostrar dados de qual jogador? 999 para encerrar '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro. Não existe jogador com o código {busca}.')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols')
        print('-' * 44)
print('<<< Volte Sempre >>>')