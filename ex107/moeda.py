def aumentar(preco, taxa):
    v = preco + (preco * taxa / 100)
    return v


def diminuir(preco, taxa):
    v = preco - (preco * taxa / 100)
    return v


def dobro(preco):
    v = preco * 2
    return v


def metade(preco):
    v = preco / 2
    return v