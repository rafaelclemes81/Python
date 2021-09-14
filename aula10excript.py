from tkinter import *

janela = Tk()

lb1 = Label(janela, text='Label 1', bg='green')
lb1.pack(side=BOTTOM)
lb2 = Label(janela, text='Label 2', bg='red')
lb2.pack(side=LEFT)
lb3 = Label(janela, text='Label 3', bg='blue')
lb3.pack(side=RIGHT)
lb4 = Label(janela, text='Label 4', bg='yellow')
lb4.pack(side=TOP)

janela.geometry('500x500+50+50')
janela.mainloop()