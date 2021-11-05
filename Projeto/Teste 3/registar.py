from tkinter import *
import tkinter as tk
from function import mysql_registar

def registar():
    app_reg = Tk()
    app_reg.resizable(width=0, height=0) 
    app_reg.title('MyHealth')
    
    def insert():
        mysql_registar(
            username1=username.get(),
            password1=password.get(),
            nome_completo1=nome_completo.get(),
            email1=email.get(),
            data_nasc1=data_nasc.get(),
            peso_inicial1=peso_inicial.get(),
            altura1=altura.get(),
            imc1=imc.get(),
            exercicio_diario1=exercicio_diario.get(),
            calorias1=calorias.get(),
            copos_de_agua1=copos_de_agua.get(),
            intervalo1=intervalo.get()
        )
    def sair():
        app_reg.destroy()

    app_reg.title('MyHealth')
    app_reg.configure(background='black')
    Label(app_reg,text='Criar Utilizador',font=("Arial", 30),bg='black',fg='#74FF00').pack()

    Label(app_reg, text="User Name",bg='black',fg='white').pack()
    username = StringVar(app_reg)
    Entry(app_reg, textvariable=username).pack()
    
    Label(app_reg, text="PassWord",bg='black',fg='white').pack()
    password = StringVar(app_reg)
    Entry(app_reg, textvariable=password).pack()

    Label(app_reg, text="Nome Completo",bg='black',fg='white').pack()
    nome_completo = StringVar(app_reg)
    Entry(app_reg, textvariable=nome_completo).pack()


    Label(app_reg,text="Email",bg='black',fg='white').pack()
    email = StringVar(app_reg)
    Entry(app_reg, textvariable=email).pack()
    

    Label(app_reg,text="Data de Nascimento",bg='black',fg='white').pack()
    data_nasc = StringVar(app_reg)
    Entry(app_reg, textvariable=data_nasc).pack()
    

    Label(app_reg,text="Peso",bg='black',fg='white').pack()
    peso_inicial = StringVar(app_reg)
    Entry(app_reg, textvariable=peso_inicial).pack()


    Label(app_reg,text="Altura",bg='black',fg='white').pack()
    altura = StringVar(app_reg)
    Entry(app_reg, textvariable=altura).pack()
    

    Label(app_reg,text="IMC",bg='black',fg='white').pack()
    imc = StringVar(app_reg)
    Entry(app_reg, textvariable=imc).pack()


    Label(app_reg,text="Exercicio Diario",bg='black',fg='white').pack()
    exercicio_diario = StringVar(app_reg)
    Entry(app_reg, textvariable=exercicio_diario).pack()
    

    Label(app_reg,text="Calorias",bg='black',fg='white').pack()
    calorias = StringVar(app_reg)
    Entry(app_reg, textvariable=calorias).pack()


    Label(app_reg,text="Copos de agua",bg='black',fg='white').pack()
    copos_de_agua = StringVar(app_reg)
    Entry(app_reg, textvariable=copos_de_agua).pack()

    Label(app_reg,text="Intervalo",bg='black',fg='white').pack()
    intervalo = StringVar(app_reg)
    Entry(app_reg, textvariable=intervalo).pack()

    
    Label(app_reg,text="",bg='black',fg='white' ,font=("Arial", 2)).pack()
    registarButton = Button(app_reg, text="Criar Utilizador", command=insert,border="0").pack()
    Label(app_reg,text="",bg='black',fg='white',font=("Arial", 2)).pack()
    voltar = Button(app_reg, text="Voltar", command=sair,border="0").pack()



    
 
    
    app_reg.mainloop()
    


