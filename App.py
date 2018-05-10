from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from SerialHandler import *
 
numberOfButtons = 3

#List that will contain the labels number and text. Ex: [(0,"Botão 1"),(1,"Botão 2")... ]
labels = [(i,str("Botão " + str(i+1))) for i in range(numberOfButtons )] 
#Functions that the user can select for the buttons  
button_functions = ["Uber","Facebook","Twitter"] 

class window:
    def __init__(self,tk):
        self.boxes = [] 
         
        """This will loop making labels_number loop throgh the first element in labels ( the numbers )
        the second element will be the text "Botão .."""
        for labels_number,labels_text in labels :

            newFrame = Frame(tk)
            newFrame.pack()

            newLabel = Label(newFrame,text=labels_text)
            newLabel.pack(side="left")

            newCombobox = ttk.Combobox(newFrame,text=labels_text,values=button_functions)
            newCombobox.pack(padx=15,pady=10)

            self.boxes.append(newCombobox)
            
            if labels_number == numberOfButtons - 1: #Create a the combobox after reaching the last button
                frameBottom = Frame(tk)
                frameBottom.pack(pady=20)
                submitBtn = Button(frameBottom, text ="Confirmar", command = self.submitFunction) #Create a button that executes the function submit when pressed
                submitBtn.pack(padx=10,pady=10)

    def submitFunction(self):  #Function that is exectuted when a button is pressed
        msg = ""
        for a in self.boxes:
            try:
                ser.write(struct.pack('>B', int(a.current())))
            except:
                msg = "Não foi possivel mudar as funções do arduino"
            else:
                msg = "Funções alteradas"
        messagebox.showwarning("Tangram",msg)
		      
mainWindow = Tk() 

"""Try to connect with the arduino. If dont, show menssage"""
try: 
    ser = serial.Serial(getPort(),9600)
except: 
    messagebox.showwarning("Tangram","Nenhum arduino conectado!")
else: 
    
    mainWindow.resizable(False, False) #Block the user to change the size of the main window
    mainWindow.title("Tangram") #Add title for the main window
    mainWindow.geometry("300x300") # Size of the main window
    labels_text = Label( mainWindow, text="Mudar funções dos botões", font=("Helvetica", 16)) 
    labels_text.pack(pady=10)
    app = window(mainWindow)

    mainWindow.mainloop() #Continue looping to keep the interface