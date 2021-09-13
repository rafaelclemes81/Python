''' CRIE UM PROGRAMA QUE TENHA UMA TUPLA COM VÁRIAS PALAVRAS (NÃO UTILIZAR ACENTOS).
DEPOIS DISSO, VOCÊ DEVE MOSTRAR, PARA CADA PALAVRA, QUAIS SÃO AS SUA VOGAIS'''
palavras = ('CRIE', 'PROGRAMA', 'TUPLA', 'PALAVRAS', 'VOGAL')
for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')