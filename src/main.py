# -*- coding: utf-8 -*-

from tkinter import *
import frames as frames

fundo1 = '#EF8D6A'

lista = ['a','a', 'a']

root = Tk()
         
class Aplication(): 
    def __init__(self):
        self.root = root
        self.tela()
        #frames.Login(self)
        frames.Caixa(self, lista)
        self.root.mainloop()               
    def tela(self):
        self.root.title("Petshop Mundocão")
        self.root.configure(background=fundo1)
        self.root.resizable(False, False)
        self.root.geometry("800x500")        

Aplication()