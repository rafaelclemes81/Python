num = int(input('Informe o número que deseja converter: '))

binaux = list()
binario = list()

# Identificando quantas casas o binário vai ter
ctrl = 0
i = 0
while True:
    if 2**i > num:
        break
    else:
        ctrl = 2**i
        binaux.append(ctrl)
    i += 1
    binaux.sort(reverse=True)

# Montando o binário
binario.append(1)
aux = ctrl
while True:
    ctrl = ctrl / 2
    if (aux + ctrl) <= num:
        binario.append(1)
        aux += ctrl
    else:
        binario.append(0)
    if ctrl / 2 < 1:
        break

# Imprimindo o binário com formatação correta
print(f'O número {num} convertido para binário é ', end='')
for k in range(0, len(binario)):
    print(f'{binario[k]}', end='')

