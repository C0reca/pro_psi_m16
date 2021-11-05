
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *

class mclass:
    def __init__(self,  window):
        self.window = window
        self.button = Button (window, text="check", command=self.plot)
        self.button.pack()

    def plot (self):
        x= np.array ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
        p= np.array ([4344,3677,3438,3918,3281,4249,4798,3785,3802,3304,4225,3860,3561,4496,4269,4466,3856,3714,4051,4325,4878,4941,4255,3691,4837,4314,3871,4333,4713,3097])
        
        fig = Figure(figsize=(6,6))
        a = fig.add_subplot()

        a.plot(x,p,color='blue')
        
        a.set_title ("Mês", fontsize=16)
        a.set_ylabel("Nº Calorias", fontsize=14)
        a.set_xlabel("Dia", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()

window= Tk()
start= mclass (window)
window.mainloop()