import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes["text"] = texto


janela = Tk()
janela.title('Visualizador de Cotações')
janela.geometry("380x300")

texto_orientacao = Label(janela, text='Clique para exibir as cotações!')
texto_orientacao.grid(column=0, row=0, padx=100, pady=10)

botao = Button(janela, text='Buscar Cotações Dólar/Euro/BTC', command=pegar_cotacoes)
botao.grid(column=0, row=5, padx=100, pady=10)

texto_cotacoes = Label(janela, text='')
texto_cotacoes.grid(column=0, row=10, padx=100, pady=10)

janela.mainloop()