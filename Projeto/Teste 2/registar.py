from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from functools import partial
import mysql.connector
from tkinter import messagebox

def registar():
    tkWindow = Tk()
    #mydb=conect()
    tkWindow.geometry('600x700')  
    tkWindow.title('MyHealth')
    
    def insert():
        print ('ola')

    def username():
        Label(tkWindow, text="User Name",bg='black',fg='white').place(x=10, y=50)
        username = StringVar()
        Entry(tkWindow, textvariable=username).place(x=10, y=75)
    
    def nome_completo():
        Label(tkWindow, text="Nome Completo",bg='black',fg='white').place(x=10, y=100)
        nome_completo = StringVar()
        Entry(tkWindow, textvariable=nome_completo).place(x=10, y=125)

    def email():
        Label(tkWindow,text="Email",bg='black',fg='white').place(x=10, y=150)
        email = StringVar()
        Entry(tkWindow, textvariable=email, show='*').place(x=10, y=175)
        
    def data_nasc():
        Label(tkWindow,text="Data de Nascimento",bg='black',fg='white').place(x=10, y=200)
        data_nasc = StringVar()
        Entry(tkWindow, textvariable=data_nasc, show='*').place(x=10, y=225)
        
    def peso_inicial():
        Label(tkWindow,text="Peso",bg='black',fg='white').place(x=10, y=250)
        peso_inicial = StringVar()
        Entry(tkWindow, textvariable=peso_inicial, show='*').place(x=10, y=275)
        
    def altura():
        Label(tkWindow,text="Altura",bg='black',fg='white').place(x=10, y=300)
        altura = StringVar()
        Entry(tkWindow, textvariable=altura, show='*').place(x=10, y=325)
        
    def imc():
        Label(tkWindow,text="IMC",bg='black',fg='white').place(x=10, y=350)
        imc = StringVar()
        Entry(tkWindow, textvariable=imc, show='*').place(x=10, y=375)
    
    def exercicio_diario():
        Label(tkWindow,text="Exercicio Diario",bg='black',fg='white').place(x=10, y=400)
        exercicio_diario = StringVar()
        Entry(tkWindow, textvariable=exercicio_diario, show='*').place(x=10, y=425)
        
    def calorias():
        Label(tkWindow,text="Calorias",bg='black',fg='white').place(x=10, y=450)
        calorias = StringVar()
        Entry(tkWindow, textvariable=calorias, show='*').place(x=10, y=475)

    def copos_de_agua():
        Label(tkWindow,text="Copos de agua",bg='black',fg='white').place(x=10, y=500)
        copos_de_agua = StringVar()
        Entry(tkWindow, textvariable=copos_de_agua, show='*').place(x=10, y=525)
        
    def intervalo():
        Label(tkWindow,text="Intervalo",bg='black',fg='white').place(x=10, y=550)
        intervalo = StringVar()
        Entry(tkWindow, textvariable=intervalo, show='*').place(x=10, y=575)

    tkWindow.title('MyHealth')
    tkWindow.configure(background='black')
    Label(tkWindow,text='Criar Utilizador',font=("Arial", 30),bg='black',fg='#74FF00').place(x=10, y=0)

    loginButton = Button(tkWindow, text="Criar Utilizador", command=insert,border="0",).place(x=10, y=610)
    loginButton = Button(tkWindow, text="Voltar", command=insert,border="0",).place(x=100, y=610)


    #Label(tkWindow,text='Dados Pessois',font=("Arial", 30),bg='black',fg='#74FF00').place(x=10, y=0)
    
    username()
    nome_completo()
    email()
    data_nasc()
    #Label(tkWindow,text='Dados Corpo',font=("Arial", 30),bg='black',fg='#74FF00').place(x=10, y=0)
    peso_inicial()
    altura()
    #Label(tkWindow,text='Dados automaticos',font=("Arial", 30),bg='black',fg='#74FF00').place(x=10, y=0)
    imc()
    exercicio_diario()
    calorias()
    #Label(tkWindow,text='Agua',font=("Arial", 30),bg='black',fg='#74FF00').place(x=10, y=0)
    copos_de_agua()
    intervalo()
    
    tkWindow.mainloop()
    
registar()

