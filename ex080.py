''' CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR CINCO VALORES NUMÉRICOS E CADASTRE-OS EM UMA LISTA
JÁ NA POSIÇÃO CORRETA DE INSERÇÃO (SEM UTILIZAR O SORT). NO FINAL MOSTRE A LISTA ORDENADA NA TELA'''
lista = list()
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]: # poderia usar na última expressão lista[len(lista)-1]
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(f'O valores digitados em ordem foram {lista}')
