from tkinter import *

def bt_click():
    lb['text'] = ed.get() # a funçao get() retorna o valor que foi digitado no objeto Entry

janela = Tk()

ed = Entry(janela)
ed.place(x=50, y=50)

bt = Button(janela, width=20, text='Ok', command=bt_click)
bt.place(x=50, y=80)

lb = Label(janela, text='Label')
lb.place(x=50, y=110)

janela.geometry('300x300+200+200')
janela.mainloop()