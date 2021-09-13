'''CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÃO COM O NOME "SANTO"'''
cidade = str(input('Informe o nome de uma cidade: ')).strip()
print('A cidade {} inicia com "Santo"?'.format(cidade))
print(cidade[:5].upper() == "SANTO")

