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


num = leiaInt('Digite um valor: ')
print(f'O número digitado foi {num}')
