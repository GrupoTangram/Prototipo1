from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from SerialHandler import *
 
numberOfButtons = 3 #Number of buttons

#List that will contain the labels number and text. Ex: [(0,"Botão 1"),(1,"Botão 2")... ]
labels = [(i,str("Botão " + str(i+1))) for i in range(numberOfButtons )] 

button_functions = ["Uber","Facebook","Twitter"] #Functions that the user can select for the buttons  

class window:
    def __init__(self,tk):
        self.boxes = [] 

        #This will loop making labels_number loop throgh the first element in labels ( the numbers )
        #the second element will be the text "Botão .."
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

        for i in self.boxes:
            keys.append(i.current())
            
        for i in keys:
            ser.write(struct.pack('>B', int(i))) #Sent to the serial the number of the function
            print(i)
		      
mainWindow = Tk() # create main window
 
try: #Try to connect with the arduino
    ser = serial.Serial(getPort(),9600) #getPort will return [] if there is no arduino connected
except: #When if fails to find an arduino connected
    messagebox.showwarning("Tangram","Nenhum arduino conectado!")
else: # If found an arduino in a port
    
    mainWindow.resizable(False, False) #Block the user to change the size of the main window
    mainWindow.title("Tangram") #Add title for the main window
    mainWindow.geometry("300x300") # Size of the main window
    labels_text = Label( mainWindow, text="Mudar funções dos botões", font=("Helvetica", 16)) 
    labels_text.pack(pady=10)
    app = window(mainWindow)

    mainWindow.mainloop() #Continue looping to keep the interface