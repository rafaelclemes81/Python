'''FAÇA UM PROGRAMA QUE LEIA O NOME E O PESO DE VÁRIAS PESSOAS, GUARDANDO TUDO EM UMA LISTA. AO FINAL MOSTRE:
A - QUANTAS PESSOAS FORAM CADASTRADAS
B - UMA LISTAGEM COM AS PESSOAS MAIS PESADAS
C - UMA LISTAGEM COM AS PESSOAS MAIS LEVES
CRITÉRIO, PESADO 100 OU MAIS, LEVE 70 OU MENOS'''
temp = list()
princ = list()
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar?: '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo foram cadastradas {len(princ)} pessoas.')
print(f'O maior peso digitado foi {mai}kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso digitado foi {men}kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
