from tkinter import *
import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure



def cli_cal_di():
    cli_cal = Tk()
    cli_cal.title('MyHealth')
    cli_cal.geometry('600x600')
    cli_cal.configure(background='black')
    
    Label(cli_cal,text='Historio Calorias',font=("Arial", 50),bg='black',fg='#74FF00').pack()
    
    def plot ():
        x= np.array ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
        p= np.array ([4344,3677,3438,3918,3281,4249,4798,3785,3802,3304,4225,3860,3561,4496,4269,4466,3856,3714,4051,4325,4878,4941,4255,3691,4837,4314,3871,4333,4713,3097])
        
        fig = Figure(figsize=(6,6))
        a = fig.add_subplot()

        a.plot(x,p,color='blue')
        
        a.set_title ("Mês", fontsize=16)
        a.set_ylabel("Nº Calorias", fontsize=14)
        a.set_xlabel("Dia", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=cli_cal)
        canvas.get_tk_widget().pack()
        canvas.draw()
    plot()
    
    cli_cal.mainloop()