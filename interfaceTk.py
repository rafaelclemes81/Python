from tkinter import *
def bt_click():
    print("Clique do botão")

    lb['text'] = 'Funcionou. Parabéns' # essa linha altera o valor da tag text da variável lb

janela = Tk()

bt = Button(janela, width=20, text='ok', command=bt_click)
bt.place(x=100, y=100)

lb = Label(janela, text="Praticando TkInter") # ATRIBUINDO A VARIÁVEL LB, UMA INSTÂNCIA DO MÉTODO LABEL
lb.place(x=100, y=200) # DEFINIDO QUE A INSTÂNCIA DO LABEL CRIADA ACIMA FAZ É DO GERECIADOR DE LAYOUT TIPO PLACE


janela.geometry('300x300+200+200') # DEFINIR TAMANHO E POSIÇÃO DA JANELA - PASSAR LAR + ALT + POS_X + POS_Y

janela.mainloop() # ESSA FUNÇÃO DEFINE QUE A JANELA SEJA EXIBIDA ATÉ FECHAR


