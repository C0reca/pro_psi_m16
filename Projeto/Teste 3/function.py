from tkinter import messagebox
from conection_bd import conect
import numpy as np


userlogin=''


def popup():
  messagebox.showerror(title=None, message="Username ou Password errado",)
  
def insert(username1,password1):
    from m_prin import createNewWindow
    global userlogin
    mydb=conect()
    mycursor = mydb.cursor()
    userlogin=username1
    passwordlogin=password1
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
        
def mysql_registar(username1,
                   password1,
                   nome_completo1, 
                   email1, 
                   data_nasc1, 
                   peso_inicial1, 
                   altura1, 
                   imc1, 
                   exercicio_diario1, 
                   calorias1, 
                   copos_de_agua1, 
                   intervalo1):
    mydb=conect()
    mycursor = mydb.cursor()
    username=username1
    passw=password1
    nome_completo=nome_completo1
    email=email1
    data_nasc=data_nasc1
    peso_inicial=peso_inicial1
    altura=altura1
    imc=imc1
    exercicio_diario=exercicio_diario1
    calorias=calorias1
    copos_de_agua=copos_de_agua1
    intervalo=intervalo1

    sql = "INSERT INTO login (username_cli,password) VALUES (%s, %s)"
    val = (username,passw)
    mycursor.execute(sql, val)
    
    sql1 = "INSERT INTO clientes ( `username_cli`, `nome_completo`, `email`, `data_nasc`, `peso_incial`, `altura`, `imc`, `exercicio_diario`, `calorias`, `copos_de_agua`, `intervalo`)  VALUES  (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val1 = (username,
            nome_completo,
            email,
            data_nasc,
            peso_inicial,
            altura,
            imc,
            exercicio_diario,
            calorias,
            copos_de_agua,
            intervalo)
    
    mycursor.execute(sql1, val1)

    mydb.commit()
    
def id_cli():
    user=userlogin
    print (user)
    mydb=conect()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM clientes where username_cli like '"+user+"'")
    result = mycursor.fetchall()

    return result


def cal_dia_db():
    mydb=conect()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM clientes_calorias_diarias where id_cliente like 3")
    result = mycursor.fetchall()
    
    print (result)
    x=0
    lista=[]
    lista1=[]
    lista2=[]
    while x<30:
        lista.insert(result[x][2])
        lista1 = lista1 + (result[x][3])
        lista2= lista2 + (result[x][4])
        x+=1
    print (lista)
    print (lista1)
    print (lista2)
    
cal_dia_db()