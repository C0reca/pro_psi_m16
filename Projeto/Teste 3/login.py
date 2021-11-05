from tkinter import *
import tkinter as tk
from functools import partial
from function import insert
from registar import registar

def insert1():
    username1=username.get()
    password1=password.get()
    insert(username1,password1)
    


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
Label(tkWindow,text=' ',font=("Arial", 5),bg='black',fg='#74FF00').pack()

loginButton = Button(tkWindow, text="Login", command=insert1,border="0",).pack()

Label(tkWindow,text=' ',font=("Arial", 2),bg='black',fg='#74FF00').pack()

registerButton = Button(tkWindow, text="Registar", command=registar,border="0",).pack()



tkWindow.mainloop()