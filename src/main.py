# -*- coding: utf-8 -*-

from tkinter import *
import frames

fundo1 = '#EF8D6A'

root = Tk()
         
class Aplication(): 
    def __init__(self):
        self.root = root
        self.tela()
        frames.Login(self)
        self.root.mainloop()               
    def tela(self):
        self.root.title("Petshop Mundocão")
        self.root.configure(background=fundo1)
        self.root.resizable(False, False)
        self.root.geometry("800x500")        

Aplication()
