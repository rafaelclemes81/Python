from tkinter import *

janela = Tk()
janela.title('Praticando TkInter')

lb1 = Label(janela, text='SIDE1', bg='white')
lb1.pack(side=LEFT)
lb2 = Label(janela, text='SIDE2', bg='red')
lb2.pack(side=LEFT)
lb3 = Label(janela, text='ANCHOR1', bg='white')
lb3.pack(anchor=NW)
lb4 = Label(janela, text='ANCHOR2', bg='red')
lb4.pack(side=BOTTOM, anchor=SW)

janela['bg'] = 'black'
janela.geometry('500x500+50+50')
janela.mainloop()