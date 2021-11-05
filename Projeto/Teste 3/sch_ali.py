from tkinter import *
import tkinter as tk
from tab_ali import listar_alimentos

def TabelaAli():
    app1 = Tk()
    app1.geometry('700x500') 
    app1.title('MyHealth')
    app1.configure(background='black')
    
    Label(app1,text='Pesquisar alimentos',font=("Arial", 50),bg='black',fg='#74FF00').pack()
    
    
    alimento1 = StringVar()
    Entry(app1, textvariable=alimento1).pack()
    
    def l_a():
        alimento=alimento1.get()
        listar_alimentos(alimento)

    tt = Button(app1, text="Pesquisar", command=l_a,border="0",).pack()
    
    Label(app1,text='Adicionar alimento ',font=("Arial", 10),bg='black',fg='#74FF00').pack()
    all_adi = StringVar()
    Entry(app1, textvariable=all_adi).pack()