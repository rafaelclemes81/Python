def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO. por favor, informe um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\n\033[34mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def linha(tam=50):
    return '-' * tam


def cabecalho(txt):
    print(linha(50))
    print(txt.center(50))
    print(linha(50))


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[31m{c} - \033[34m{item}')
        c += 1
    print(linha())
    opc = leiaInt('\033[35mEscolha uma opção: \033[m')
    return opc
