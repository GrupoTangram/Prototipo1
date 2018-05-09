from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from SerialHandler import *


data = ["Uber","Facebook","Twitter"]    

labels = [(0,"Botão 1:"), (1,"Botão 2:"), (2,"Botão 3:")]
keys = []

class window:
    def __init__(self,tk):
        self.boxes = [] 
        
        for index,label in labels :

            f = Frame(tk)
            f.pack()

            l = Label(f,text=label)
            l.pack(side="left")

            c = ttk.Combobox(f,text=label,values=data)
            c.pack(padx=15,pady=10)
            self.boxes.append(c)

            if(index == 2):
                frameBottom = Frame(tk)
                frameBottom.pack(pady=20)
                
                submitBtn = Button(frameBottom, text ="Confirmar", command = self.submit)
                submitBtn.pack(padx=10,pady=10)

    def submit(self):  
        global keys 

        for a in self.boxes:
            keys.append(a.current())
            
        for a in keys:
            ser.write(struct.pack('>B', int(a)))
            print(a)

		      
root = Tk()
try:
    ser = serial.Serial(getPort(),9600)
except:
    messagebox.showwarning("Tangram","Nenhum arduino conectado!")
else:
    root.resizable(False, False)
    root.title("Tangram")
    root.geometry("300x300")
    label = Label( root, text="Mudar funções dos botões", font=("Helvetica", 16))
    label.pack(pady=10)
    app = window(root)

    root.mainloop()


