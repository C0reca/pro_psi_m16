from tkinter import *
import tkinter as tk
from tkinter import ttk
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
      
      #scrollbar = Scrollbar(app3)
      #scrollbar.pack( side = RIGHT, fill = Y )
      #tabela = Listbox(app3, width=100, height=200)
      #tabela.pack()
      tree=ttk.Treeview(app3)
      tree['show'] = 'headings'

      s= ttk.Style(app3)
      s.theme_use("clam")
      s.configure(".", font=('arial', 11))
      s.configure("Treeview.Heading", foreground='white', font=('arial', 11, 'bold'), relief="groove", background="pink")
      
      
      tree["columns"]=("id_ali","nome_ali","marca_ali","calorias","ativo")
      
      tree.column("id_ali", width=50, minwidth=50, anchor=tk.CENTER)
      tree.column("nome_ali", width=50, minwidth=50, anchor=tk.CENTER)
      tree.column("marca_ali", width=50, minwidth=50, anchor=tk.CENTER)
      tree.column("calorias", width=50, minwidth=50, anchor=tk.CENTER)
      tree.column("ativo", width=50, minwidth=50, anchor=tk.CENTER)
      
      tree.heading("id_ali",text="ID",anchor=tk.CENTER)
      tree.heading("nome_ali",text="Nome",anchor=tk.CENTER)
      tree.heading("marca_ali",text="Marca",anchor=tk.CENTER)
      tree.heading("calorias",text="Calorias",anchor=tk.CENTER)
      tree.heading("ativo",text="Ativo",anchor=tk.CENTER)

      
      app3.geometry('500x500')
      
      alimento=alimento1.get()
      mydb=conect()
      mycursor = mydb.cursor()
      mycursor.execute("SELECT * FROM alimentos where nome_ali like '%"+alimento+"%' ")
      dados = mycursor.fetchall()
      
      #print (dados)
      #if len(dados)>0:
      i=0
      for ro in dados:
          tree.insert('', i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4]))
          i+=1
            #tree.insert('',record,text='',values=("ola","adeus"))
        #tabela.config(yscrollcommand=scrollbar.set)
        #scrollbar.config(command=tabela.yview)
      #else:
        #Label(app3, text="Nenhum alimento com esse nome",bg='black',fg='white').place(x=10, y=50)
      mydb.close()
      
      
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

