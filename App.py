#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from SerialHandler import *
import struct 
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("/home/joao/Tangram/adminKey.json")
firebase_admin.initialize_app(cred)

functions = [["Pedir uber"],["Ligar para contato"]]

functionsImage = {
   '0': 'firstPage.gif',
   '1': 'Chamando_Uber.gif',
   '2': 'Emergencia.gif',
   '3': 'Uber.gif'
}

mainWindow = Tk() 

def main():
    try: 
        ser = serial.Serial("/dev/ttyUSB0",9600)
    except: 
        messagebox.showwarning("Tangram","Nenhum arduino conectado!")
    else: 
        
        ser.write(struct.pack(">B", 1))
        while True:
            print(ser.readline()[0:8])
        for a in functions:
            a.append(int(ser.readline()[0:3]))
            print(a)

        print("oi")

        mainWindow.resizable(False, False)
        mainWindow.title("Tangram") 
        mainWindow.geometry("600x600")

        labels_text = Label( mainWindow, text="Bem vindo de volta, Sr Ricardo Moura.", font=("Helvetica", 16)) 
        labels_text.pack()
        
        canvas = Canvas(mainWindow, width = 600, height = 600)
        canvas.pack() 

        while True:
            updateData(functions)
            pageImage = PhotoImage(file = 'firstPage.gif')
            canvas.create_image(0,0,anchor = NW, image = pageImage)
            mainWindow.update() 
            print(functions)
            funcTag = 0
            while funcTag == 0:
                funcTag = int(ser.readline()[0]) 
            functions[funcTag-1][1] +=1
            pageImage = PhotoImage(file = functionsImage[str(funcTag)])
            canvas.create_image(0,0,anchor = NW, image = pageImage) 
            mainWindow.update()

            time.sleep(5)

        
        
def updateData(lista):
    db = firestore.client()
    doc_ref = db.collection(u'alunos').document(u'1')
    doc_ref.update({
        u'funcoes':{
            lista[0][0]:lista[0][1],
            lista[1][0]:lista[1][1]
        }
    })


if __name__ == "__main__":
    main()


        
        