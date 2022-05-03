# -*- coding: utf-8 -*-

from ast import Return
from tkinter import messagebox
from tkinter import *
import Frames
import gerenciador_BD

fundo1 = '#4B0082'
fundo2 = '#7B68EE'
fundo3 = '#8A2BE2'
borda = '#BA55D3'

root = Tk()
         
class Aplication(): 
    def __init__(self):
        self.root = root
        self.tela()
        self.login()
        self.root.mainloop()               
    def tela(self):
        self.root.title("teste")
        self.root.configure(background="#14568F")
        self.root.resizable(False, False)
        self.root.geometry("800x500")        
    
    def login(self):
        self.frame_1 = Frame(self.root, highlightbackground="#218CEB", borderwidth=0.01, highlightthickness=2)
        self.frame_1.place(relx=0.01, rely=0.01, relheight=0.98, relwidth=0.98)

        self.root.title("login")
        self.atual_frame = self.frame_1
        
        #Criando os Labels e Entradas

        #instrução
        self.label1 = Label(self.frame_1, text="Digite as informação para logar-se")
        self.label1.place(relx= 0.38, rely = 0.1)
        
        #CPF
        self.label1 = Label(self.frame_1, text="CPF")
        self.label1.place(relx= 0.48, rely = 0.2)
        
        self.et_cpf = Entry(self.frame_1)
        self.et_cpf.place(relx= 0.4, rely = 0.25)
        self.et_cpf.focus()
       
        #senha
        self.label2 = Label(self.frame_1, text="Senha")
        self.label2.place(relx= 0.47, rely = 0.3)
        
        self.et_Senha = Entry(self.frame_1)
        self.et_Senha.place(relx= 0.4, rely = 0.35)

        #Criando os Botões
        self.bt_OK = Button(self.frame_1, text="OK", command= lambda: self.muda_tela(gerenciador_BD.BD.verifica_senha(self, self.et_cpf.get(), self.et_Senha.get())))
        self.bt_OK.place(relx= 0.47, rely = 0.42)

 
    def muda_tela(self, lista):
        for i in lista:
            cargo = i[3]
        if cargo == 'ESTOQUISTA':
            self.atual_frame.destroy()
            Frames.Estoquista(self)
        elif(cargo == 'RECEPCIONISTA'):
            self.atual_frame.destroy()
            Frames.Recepcionista(self)
        elif(cargo == 'CAIXA'):
            self.atual_frame.destroy()
            Frames.Caixa(self)
        elif(cargo == []):
            self.msgLimpar = messagebox.showerror('ERRO', 'Funcionário não encontrado')

Aplication()
