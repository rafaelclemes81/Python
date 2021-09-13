''' APRIMORE O EXERCÍCIO 086 MOSTRANDO AO FINAL:
A - A SOMA DE TODOS OS VALORES PARES DIGITADOS
B - A SOMA DOS VALORES DA TERCEIRA COLUNA
C - O MAIOR VALOR DA SEGUNDA LINHA'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somacoluna = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l+1}, {c+1}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            somacoluna += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maior:
                maior = matriz[l][c]
print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}] ', end='')
    print()
print(f'A soma de todos os valores pares digitados foi {somapar}')
print(f'A soma de todos os elementos da terceira coluna foi {somacoluna}')
print(f'O maior valor da segunda linha é {maior}')
