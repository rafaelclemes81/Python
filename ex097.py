''' FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA 'ESCREVA()', QUE RECEBE UM TEXTO
QUALQUER COMO PARÂMETRO E MOSTRE UMA MENSAGEM COM TAMANHO ADAPTÁVEL'''
def escreva(txt):
    print('~' * (len(txt)+2))
    print(f' {txt} ')
    print('~' * (len(txt)+2))


#Programa Principal
escreva('Programa Teste')