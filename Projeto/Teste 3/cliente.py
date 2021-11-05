from tkinter import *
import tkinter as tk
from function import id_cli

def cliente_menu():
    cli_menu = Tk()
    cli_menu.title('MyHealth')
    cli_menu.geometry('500x500')
    
    cli_menu.configure(background='black')
    
    Label(cli_menu,text='Cliente',font=("Arial", 50),bg='black',fg='#74FF00').pack()
    
    result=id_cli()
    print (result)
    
    Label(cli_menu,text='Dados',bg='black',fg='#74FF00').pack()
    Label(cli_menu,text='Username = '+result[0][1],bg='black',fg='#74FF00').pack()
    Label(cli_menu,text='Nome Completo = '+result[0][2],bg='black',fg='#74FF00').pack()
    Label(cli_menu,text='Email = '+result[0][3],bg='black',fg='#74FF00').pack()
    Label(cli_menu,text='Data de nascimento = '+result[0][4],bg='black',fg='#74FF00').pack()
    Label(cli_menu,text='Peso Inicial = '+result[0][5],bg='black',fg='#74FF00').pack()
    Label(cli_menu,text='Altura = '+result[0][6],bg='black',fg='#74FF00').pack()
    Label(cli_menu,text='IMC inicial = '+result[0][7],bg='black',fg='#74FF00').pack()
    Label(cli_menu,text='Exercicio diario = '+result[0][8],bg='black',fg='#74FF00').pack()
    Label(cli_menu,text='Calorias diarias = '+result[0][9],bg='black',fg='#74FF00').pack()
    Label(cli_menu,text='Copos de agua = '+result[0][10],bg='black',fg='#74FF00').pack()
    Label(cli_menu,text='Ineralo copo de agua = '+result[0][11],bg='black',fg='#74FF00').pack()
    

    cli_menu.mainloop()