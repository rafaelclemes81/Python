# CONVERSOR DE BINARIO PARA DECIMAL

bin = str(input('Informe um número binário: '))
bin = bin[::-1]
dec = 0;
for i, v in enumerate(bin):
    if bin[i] == '1':
        dec += 2**i

print(f'O número binário {bin}, convertido para decimal é: {dec}')

