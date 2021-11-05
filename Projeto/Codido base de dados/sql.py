from tkinter import *
from PIL import ImageTk, Image
import os
from functools import partial
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="dados"
)

def insert():

        mycursor = mydb.cursor()

        userlogin=username.get()
        passwordlogin=password.get()

        sql = "INSERT INTO login VALUES (%s, %s)"
        val = (userlogin,passwordlogin)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	insert()
	return

#window
tkWindow = Tk()  
tkWindow.geometry('400x400')  
tkWindow.title('MyHealth')

img = ImageTk.PhotoImage(Image.open("logo.png"))
imglabel = Label(tkWindow, image=img).grid(row=10, column=1)        

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  



tkWindow.mainloop()
