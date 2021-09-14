from functools import partial
from tkinter import *

def bt_soma():
    if str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric():
        n1 = float(ed1.get())
        n2 = float(ed2.get())
        soma = n1 + n2
        lb['text'] = soma
    else:
        lb['text'] = 'Os valores informados não são numéricos.'

janela = Tk()

ed1 = Entry(janela)
ed1.place(x=10, y=10)
ed2 = Entry(janela)
ed2.place(x=10, y=40)

bt = Button(janela, width=20, text='Soma', command=bt_soma)
bt.place(x=10, y=70)

lb = Label(janela, text='Resultado: ')
lb.place(x=10, y=100)

janela.geometry("400x300+200+200")
janela.mainloop()