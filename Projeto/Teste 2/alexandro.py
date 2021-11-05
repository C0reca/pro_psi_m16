from tkinter import *
import tkinter as tk
from tkinter import ttk
from typing import Sized
from PIL import ImageTk, Image
from functools import partial
import mysql.connector
from tkinter import messagebox


def conect():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Myhealth"
  )
  return mydb

def insert():
  mydb=conect()
  mycursor = mydb.cursor()
  userlogin=username.get()
  passwordlogin=password.get()
  mycursor.execute("SELECT * FROM login")
  result = mycursor.fetchall()
  #Verificar se dados sao validos
  flag=0
  for record in result:
    if userlogin == record[0] and passwordlogin == record[1]:
      flag=1
      break
  mydb.close()
  if flag==1:
        createNewWindow()
  else:
        popup()
        
def createNewWindow():
  app2=Toplevel(tkWindow) 
  app2.geometry('500x500')
  loginButton = Button(app2, text="Alimentos", command=TabelaAli).pack()
  app2.mainloop()

def TabelaAli():
  app1=Toplevel(tkWindow) 
  app1.geometry('500x500')
  
  
  Label(app1, text="Pesquisar Alimento",bg='black',fg='white').place(x=10, y=50)
  alimento1 = StringVar()
  Entry(app1, textvariable=alimento1).place(x=10, y=75)
  
  
  def listar_alimentos():
    app3=Toplevel(tkWindow) 
    app3.resizable(width=0, height=0)
    
    alimento=alimento1.get()
    connect=conect()
    conn = connect.cursor()
    conn.execute("SELECT * FROM alimentos where nome_ali like '%"+alimento+"%'")
    dados = conn.fetchall()
    
    
    
        
    tree=ttk.Treeview(app3)
    tree['show'] = 'headings'
    tree.pack(side="left")
    
    
    scrollbar = Scrollbar(app3, command=tree.yview)
    scrollbar.pack( side = RIGHT, fill = Y )
    

    s= ttk.Style(app3)

    s.theme_use("clam")
    s.configure(".", font=('arial', 11))
    s.configure("Treeview.Heading", foreground='white', font=('arial', 11, 'bold'), relief="groove", background="black")


    #Define number of columns
    tree["columns"]=("id_ali","nome_ali","marca_ali","calorias","ativo")
      
    tree.column("id_ali", width=70, minwidth=70, anchor=tk.CENTER ,stretch=True)
    tree.column("nome_ali", width=400, minwidth=400, anchor=tk.CENTER, stretch=True)
    tree.column("marca_ali", width=200, minwidth=200, anchor=tk.CENTER, stretch=True)
    tree.column("calorias", width=70, minwidth=70, anchor=tk.CENTER,stretch=True)
    tree.column("ativo", width=150, minwidth=150, anchor=tk.CENTER,stretch=True)
    
    tree.heading("id_ali",text="ID",anchor=tk.CENTER)
    tree.heading("nome_ali",text="Nome",anchor=tk.CENTER)
    tree.heading("marca_ali",text="Marca",anchor=tk.CENTER)
    tree.heading("calorias",text="Calorias",anchor=tk.CENTER)
    tree.heading("ativo",text="Ativo",anchor=tk.CENTER)

    i=0

    for ro in dados:
        tree.insert('', i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4]))
        i = i + 1
    tree.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=tree.yview)
    tree.pack()

    app3.mainloop()

      
      
  tt = Button(app1, text="Pesquisar", command=listar_alimentos,border="0",).pack()
  



def popup():
  #tkWindow.geometry("500x500")
  messagebox.showerror(title=None, message="Username ou Password errado",)


  

#window
tkWindow = Tk()
'''tkWindow.tk.call('wm', 'iconphoto', tkWindow._w, tk.PhotoImage(file='icon.png'))'''
tkWindow.geometry('500x300')  
tkWindow.title('MyHealth')
tkWindow.configure(background='black')

'''img = ImageTk.PhotoImage(Image.open("logo.png"))
imglabel = Label(tkWindow, image=img).grid(row=10, column=1)     '''


texto=Label(tkWindow,text='MyHealth',font=("Arial", 50),bg='black',fg='#74FF00').pack()

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name",bg='black',fg='white').pack()
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).pack() 

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password",bg='black',fg='white').pack()
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').pack()

validateLogin = partial(insert, username, password)

#login button
texto=Label(tkWindow,text=' ',font=("Arial", 10),bg='black',fg='#74FF00').pack()

loginButton = Button(tkWindow, text="Login", command=insert,border="0",).pack()

#loginButton = Button(tkWindow, text="Registar", command=registar,border="0",).pack()



tkWindow.mainloop()

