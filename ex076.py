'''CRIE UM PROGRAMA QUE TENHA UMA TUPLA ÚNICA COM NOMES DE PRODUTOS E SEUS RESPECTIVOS PREÇOS NA SEQUENCIA.
NO FINAL, MOSTRE UMA LISTAGEM DE PREÇOS ORGANIZANDO OS DADOS EM FORMA TABULAR'''
produtos = 'Arroz', 3.49, 'Feijão', 5.29, 'Macarrão', 1.89, 'Molho de Tomate', 0.75
print ('-' * 50)
print('{:^50}'.format('TABELA DE PREÇOS DE PRODUTOS'))
print ('-' * 50)
for i in range(0, len(produtos), 2 ):
    print(f'{produtos[i]:.<39} R$ {produtos[i+1]:>7.2f}')
print ('-' * 50)
print('Fim do programa ... ')

