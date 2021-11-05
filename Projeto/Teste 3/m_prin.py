from tkinter import *
import tkinter as tk
from sch_ali import TabelaAli
from cliente import cliente_menu
from cli_calorias import cli_cal_di

def createNewWindow():
    app2 = Tk()
    app2.title('MyHealth')
    app2.geometry('500x500')
    app2.configure(background='black')
    
    Label(app2,text='Menu Principal',font=("Arial", 50),bg='black',fg='#74FF00').pack()
    
    Button(app2, text="Alimentos", command=TabelaAli).pack()
    Button(app2, text="Cliente", command=cliente_menu).pack()
    Button(app2, text="Hitorico Calorias Diarias", command=cli_cal_di).pack()
    
    app2.mainloop()