'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou
V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''
while True:
    turno = str(input('''Em que turno você estuda? 
    [M] - Matutino
    [V] - Vespertino
    [N] - Noturno ''')).strip().upper()
    if turno not in 'MVN':
        print('Turno Inválido. Tente novamente!!!')
    else:
        if turno == 'M':
            print('Bom dia!!! Seja bem-vindo')
            break
        elif turno == 'V':
            print('Boa tarde!!! Seja bem-vindo')
            break
        else:
            print('Boa noite!!! Seja bem-vindo')
            break
