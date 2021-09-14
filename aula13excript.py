''' GERENCIADOR PACK, PROPRIEDADE FILL - EXPANDE PARA OS EIXOS X, Y OU AMBOS(BOTH), A ÁREA DEFINIDA
PELA PROPRIEDADE SIDE'''

from tkinter import *

janela = Tk()

lb1 = Label(janela, text='Horizontal', bg='red')
lb1.pack(side=TOP, fill=X)

lb2 = Label(janela, text='Horizontal', bg='black')
lb2.pack(side=LEFT, fill=Y)

lb3 = Label(janela, text='Horizontal', bg='black')
lb3.pack(side=RIGHT, fill=Y)

janela.geometry('500x200+600+200')

janela.mainloop()