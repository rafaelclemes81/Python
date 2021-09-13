'''CRIE UM PROGRAMA QUE LEIA UMA FRASE E DIGA SE ELA É OU NÃO UM PALÍNDROMO, DESCONSIDERANDO OS
ESPAÇOS'''
frase = str(input('Digite uma frase: ').strip().upper())
palavras = frase.split()
junto = ''.join(palavras)
#inverso = ''
inverso = junto[::-1] #essa é outra forma de fazer, utilizando fatiamento, sem o FOR
'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print(junto, inverso)
if inverso == junto:
    print('A string informada é um palíndromo.')
else:
    print('A string informada NÃO é um palíndromo.')
