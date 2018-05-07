from tkinter import *
from tkinter import ttk

import SerialHandler
import json

data = ["a","b","c",]    

labels = [(0,"Botão 1:"), (1,"Botão 2:"), (2,"Botão 3:")]

sender = SerialHandler.SerialHandler()

class window:
    def __init__(self,tk):
        self.arduinoStatusText = "Carrregando..."
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
                self.arduinoStatusLabel = Label(frameBottom,text="Carregando...")
                self.arduinoStatusLabel.pack(side="left")

                submitBtn = Button(frameBottom, text ="Confirmar", command = self.submit)
                submitBtn.pack(padx=10,pady=10)
        
    
    def submit(self):  
        keys = [] 
        for a in self.boxes:
            keys.append(a.current())

        try:
            
            sender.sendValues(keys)
        except IOError:
            self.arduinoStatusLabel['fg']='RED'
           
root = Tk()
root.resizable(False, False)
root.title("Tangram")
root.geometry("300x300")
label = Label( root, text="Mudar funções dos botões", font=("Helvetica", 16))
label.pack(pady=10)
app = window(root) 

def update():

    app.arduinoStatusLabel['text'] = sender.tryConnection()
    app.arduinoStatusLabel['fg'] = 'BLACK'
    root.after(2000, update)
root.after(2000, update)

root.mainloop()


