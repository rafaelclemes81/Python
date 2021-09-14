'''GERENCIADOR PACK, PROPRIEDADE EXPAND, DEFINE QUE TODOS OS WIDGETS DA TELA, TENHAM OS MESMOS
TAMANHOS'''

from tkinter import *

janela = Tk()

lb1 = Label(janela, text='LINHA 1', bg='blue')
lb1.pack(side=TOP, fill=BOTH, expand=1)

lb2 = Label(janela, text='LINHA 2', bg='yellow')
lb2.pack(side=TOP, fill=BOTH, expand=1)

lb3 = Label(janela, text='LINHA 3', bg='blue')
lb3.pack(side=TOP, fill=BOTH, expand=1)

lb4 = Label(janela, text='LINHA 3', bg='yellow')
lb4.pack(side=TOP, fill=BOTH, expand=1)

janela.geometry('500x200+600+200')

janela.mainloop()