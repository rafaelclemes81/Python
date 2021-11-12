from tkinter import *
def bt_click():

    import pyautogui
    import cv2
    import numpy as np

    resolution = (1920, 1080)
    codec = cv2.VideoWriter_fourcc(*"XVID")
    filename = "video.avi"
    fps = 60.0

    out = cv2.VideoWriter(filename, codec, fps, resolution)
    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Live", 480, 270)

    while True:

        img = pyautogui.screenshot()

        frame = np.array(img)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        out.write(frame)

        cv2.imshow('Live', frame)

        if cv2.waitKey(1) == ord('e'):
            break
    out.release()
    cv2.destroyAllWindows()

janela = Tk('')

bt = Button(janela, width=20, text='Iniciar Gravação', command=bt_click)
bt.place(x=80, y=130)

lb = Label(janela, text="Gravador") # ATRIBUINDO A VARIÁVEL LB, UMA INSTÂNCIA DO MÉTODO LABEL
lb.place(x=130, y=20) # DEFINIDO QUE A INSTÂNCIA DO LABEL CRIADA ACIMA FAZ É DO GERECIADOR DE LAYOUT TIPO PLACE


janela.geometry('300x300+400+400') # DEFINIR TAMANHO E POSIÇÃO DA JANELA - PASSAR LAR + ALT + POS_X + POS_Y

janela.mainloop() # ESSA FUNÇÃO DEFINE QUE A JANELA SEJA EXIBIDA ATÉ FECHAR


