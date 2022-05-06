# -*- coding: utf-8 -*-

from tkinter import *
import Frames

fundo1 = '#4B0082'
fundo2 = '#7B68EE'
fundo3 = '#8A2BE2'
borda = '#BA55D3'

root = Tk()
         
class Aplication(): 
    def __init__(self):
        self.root = root
        self.tela()
        Frames.login(self)
        self.root.mainloop()               
    def tela(self):
        self.root.title("teste")
        self.root.configure(background=fundo1)
        self.root.resizable(False, False)
        self.root.geometry("800x500")        

Aplication()
