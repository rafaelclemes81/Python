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