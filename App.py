from tkinter import *
from tkinter import ttk
funcoes = ('Uber','Ligação','Mensagem')
class window:
    def __init__(self,tk):
        self.frameBtn1 = Frame(tk)
        self.frameBtn1.pack()
        self.frameBtn2 = Frame(tk)
        self.frameBtn2.pack()
        self.frameBtn3 = Frame(tk)
        self.frameBtn3.pack()
        
        lable1 = Label(self.frameBtn1, text="Botão 1:")
        lable1.pack(side="left")
        btn1 = ttk.Combobox(self.frameBtn1, values=funcoes)
        btn1.current(2)
        btn1.pack(padx=15,pady=10)

        lable2 = Label(self.frameBtn2, text="Botão 2:")
        lable2.pack(side="left")
        btn2 = ttk.Combobox(self.frameBtn2, values=funcoes)
        btn2.current(1)
        btn2.pack(padx=15,pady=10)

        lable3 = Label(self.frameBtn3, text="Botão 3:")
        lable3.pack(side="left")
        btn3 = ttk.Combobox(self.frameBtn3, values=funcoes)
        btn3.current(0)
        btn3.pack(padx=15,pady=10)

        submitBtn = Button(tk, text ="Confirmar", command = self.submit)
        submitBtn.pack(padx=10)

    def submit(self):   # Ao pressionar o botão submit, fazer alguma coisa
        print("oi")
        

root = Tk()
root.resizable(False, False)
root.title("Tangram")
root.geometry("300x300")
label = Label( root, text="Mudar funções dos botões", font=("Helvetica", 16))
label.pack(pady=10)
app = window(root)
root.mainloop()
