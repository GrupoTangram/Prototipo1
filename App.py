#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from SerialHandler import *
import struct 



class window:
    def __init__(self,tk):
        frameBottom = Frame(tk)
        frameBottom.pack(pady=20)
        submitBtn = Button(frameBottom, text ="Confirmar", command = self.submitFunction) #Create a button that executes the function submit when pressed
        submitBtn.pack(padx=10,pady=10)
    def submitFunction(self):
        print("oi")


mainWindow = Tk() 



try: 
    ser = serial.Serial("/dev/ttyUSB0",9600)
except: 
    messagebox.showwarning("Tangram","Nenhum arduino conectado!")
else: 
    functions = [[1,"Pedir uber",0],[2,"Ligar para contato",0]]
    
    ser.write(struct.pack(">B", 1));
    
    for a,b,c in functions:
        c += int(ser.readline().replace("\r\n",""))
        print(c)
    for a,b,c in functions:
        print(c)

    mainWindow.resizable(False, False)
    mainWindow.title("Tangram") 
    mainWindow.geometry("300x300") 
    labels_text = Label( mainWindow, text="Mudar funções dos botões", font=("Helvetica", 16)) 
    labels_text.pack(pady=10)
    app = window(mainWindow)
    mainWindow.mainloop() 