from tkinter import *
from PIL import ImageTk, Image

path = 'C:/Users/mediacenter/Pictures/321.jpg'

janela = Tk()
janela.geometry("1100x540+100+100")

img = ImageTk.PhotoImage(Image.open(path))
lb23 = Label(janela, image=img)
#  lb23.grid(row=0, column=9)

lb1 = Label(janela, text='FORMA')
lb1.grid(row=0, column=0)
ed1 = Entry(janela, width=20)
ed1.grid(row=0, column=1)

lb2 = Label(janela, text='PEDIDO')
lb2.grid(row=0, column=2)
ed2 = Entry(janela, width=20)
ed2.grid(row=0, column=3)

lb3 = Label(janela, text='DT. ENTREGA')
lb3.grid(row=0, column=4)
ed3 = Entry(janela, width=20)
ed3.grid(row=0, column=5)

lb4 = Label(janela, text='MARCA')
lb4.grid(row=0, column=6)
ed4 = Entry(janela, width=20)
ed4.grid(row=0, column=7)

lb5 = Label(janela, text='MODELO')
lb5.grid(row=1, column=0)
ed5 = Entry(janela, width=20)
ed5.grid(row=1, column=1)

lb6 = Label(janela, text='COMBINAÇÃO')
lb6.grid(row=1, column=2)
ed6 = Entry(janela, width=20)
ed6.grid(row=1, column=3)

lb7 = Label(janela, text='1-CABEDAL')
lb7.grid(row=2, column=0)
ed7 = Entry(janela, width=20)
ed7.grid(row=2, column=1)

lb8 = Label(janela, text='2-DETALHE')
lb8.grid(row=3, column=0)
ed8 = Entry(janela, width=20)
ed8.grid(row=3, column=1)

lb9 = Label(janela, text='3-DETALHE')
lb9.grid(row=4, column=0)
ed9 = Entry(janela, width=20)
ed9.grid(row=4, column=1)

lb10 = Label(janela, text='4-DETALHE')
lb10.grid(row=5, column=0)
ed10 = Entry(janela, width=20)
ed10.grid(row=5, column=1)

lb11 = Label(janela, text='5-DETALHE')
lb11.grid(row=6, column=0)
ed11 = Entry(janela, width=20)
ed11.grid(row=6, column=1)

lb12 = Label(janela, text='6-DETALHE')
lb12.grid(row=7, column=0)
ed12 = Entry(janela, width=20)
ed12.grid(row=7, column=1)

lb12 = Label(janela, text='7-DETALHE')
lb12.grid(row=8, column=0)
ed12 = Entry(janela, width=20)
ed12.grid(row=8, column=1)

lb13 = Label(janela, text='FORRO')
lb13.grid(row=2, column=2)
ed13 = Entry(janela, width=20)
ed13.grid(row=2, column=3)

lb14 = Label(janela, text='GOTA')
lb14.grid(row=3, column=2)
ed14 = Entry(janela, width=20)
ed14.grid(row=3, column=3)

lb15 = Label(janela, text='ELÁSTICO')
lb15.grid(row=4, column=2)
ed15 = Entry(janela, width=20)
ed15.grid(row=4, column=3)

lb16 = Label(janela, text='PALMILHA')
lb16.grid(row=5, column=2)
ed16 = Entry(janela, width=20)
ed16.grid(row=5, column=3)

lb17 = Label(janela, text='CARIMBO')
lb17.grid(row=6, column=2)
ed17 = Entry(janela, width=20)
ed17.grid(row=6, column=3)

lb18 = Label(janela, text='SOLA')
lb18.grid(row=7, column=2)
ed18 = Entry(janela, width=20)
ed18.grid(row=7, column=3)

lb19 = Label(janela, text='CAPA DA SOLA')
lb19.grid(row=8, column=2)
ed19 = Entry(janela, width=20)
ed19.grid(row=8, column=3)

lb20 = Label(janela, text='FIVELA')
lb20.grid(row=8, column=2)
ed20 = Entry(janela, width=20)
ed20.grid(row=8, column=3)

lb21 = Label(janela, text='AVIAMENTO 1')
lb21.grid(row=8, column=2)
ed21 = Entry(janela , width=20)
ed21.grid(row=8, column=3)

lb22 = Label(janela, text='AVIAMENTO 2')
lb22.grid(row=8, column=2)
ed22 = Entry(janela, width=20)
ed22.grid(row=8, column=3)

janela.mainloop()