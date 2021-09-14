from functools import partial
from tkinter import *

def bt_click(bt):
    bt['text'] = 'Funcionou'


janela = Tk()

bt1 = Button(janela, width=20, text='Ok')
bt1['command'] = partial(bt_click, bt1) # essa linha mostra como passar o bt1 como parâmetro para a função bt_click que chamada pelo command
bt1.place(x=20, y=20)
bt2 = Button(janela, width=20, text='Ok')
bt2['command'] = partial(bt_click, bt2)
bt2.place(x=20, y=50)

janela.geometry("500x500+20+20")
janela.mainloop()