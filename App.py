from tkinter import *
from tkinter import ttk

from SerialHandler import *


data = ["a","b","c",]    

labels = [(0,"Botão 1:"), (1,"Botão 2:"), (2,"Botão 3:")]

ser = serial.Serial("COM13",9600)

class window:
    def __init__(self,tk):
        self.boxes = []
        
        for index,a in labels :
            f = Frame(tk)
            f.pack()
            l = Label(f,text=a)
            l.pack(side="left")
            c = ttk.Combobox(f,text=a,values=data)
            c.pack(padx=15,pady=10)
            self.boxes.append(c)
            if(index == 2):
                frameBottom = Frame(tk)
                frameBottom.pack(pady=20)
                
                submitBtn = Button(frameBottom, text ="Confirmar", command = self.submit)
                submitBtn.pack(padx=10,pady=10)

    def submit(self):  
        keys = []
        for a in self.boxes:
            keys.append(a.current())
        for a in keys:
            ser.write(struct.pack('>B', int(a)))
            print(a)
			      
root = Tk()
root.resizable(False, False)
root.title("Tangram")
root.geometry("300x300")
label = Label( root, text="Mudar funções dos botões", font=("Helvetica", 16))
label.pack(pady=10)
app = window(root)

def update():
    global ser
    try:
        port = getPort()
    except IOError:
        print("Arduino não conectado!")
        root.after(2000, update)
    else:
        print("conectou")
        
root.after(2000, update)
root.mainloop()


