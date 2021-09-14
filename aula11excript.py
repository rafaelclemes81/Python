from tkinter import *

janela = Tk()
janela.title('Praticando TkInter')

lb1 = Label(janela, text='BOTTOM', bg='white')
lb1.pack(side=BOTTOM)
lb2 = Label(janela, text='LEFT', bg='white')
lb2.pack(side=LEFT)
lb3 = Label(janela, text='RIGHT', bg='white')
lb3.pack(side=RIGHT)
lb4 = Label(janela, text='TOP', bg='white')
lb4.pack(side=TOP)

janela['bg'] = 'black'
janela.geometry('500x500+50+50')
janela.mainloop()