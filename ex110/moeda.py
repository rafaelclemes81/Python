def aumentar(preco=0, taxa=0, formato=False):
    v = preco + (preco * taxa / 100)
    return v if format is False else moeda(v)


def diminuir(preco=0, taxa=0, formato=False):
    v = preco - (preco * taxa / 100)
    return v if format is False else moeda(v)


def dobro(preco=0, formato=False):
    v = preco * 2
    return v if format is False else moeda(v)


def metade(preco=0, formato=False):
    v = preco / 2
    return v if format is False else moeda(v)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:8.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):
    print('-' * 50)
    print('RESUMO DO VALOR'.center(50))
    print('-' * 50)
    print(f'Preço informado {moeda(preco)}')
    print(f'{moeda(preco)} com acréscimo de {taxaa}% = {aumentar(preco, taxaa, True)}')
    print(f'{moeda(preco)} com desconto de {taxar}% = {diminuir(preco, taxar, True)}')
    print(f'Metade de {moeda(preco)} = {metade(preco, True)}')
    print(f'Dobro de {moeda(preco)} = {dobro(preco, True)}')
    print('-' * 50)