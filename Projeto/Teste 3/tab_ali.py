from tkinter import *
import tkinter as tk
from tkinter import ttk
from conection_bd import conect

def listar_alimentos(alimento1):
    app3 = Tk()
    app3.title('MyHealth')
    app3.resizable(width=0, height=0)
    
    alimento=alimento1
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
