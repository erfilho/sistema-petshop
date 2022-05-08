# -*- coding: utf-8 -*-

from email.mime import image
from tkinter import *
from tkinter import messagebox
import gerenciador_BD

fundo1 = '#E85B28'
fundo2 = '#EE6D3D'
fundo3 = '#EF8D6A'
option = '#8C4227'
borda = '#BA55D3'
fonte = "Jura"
texto = '#ffffff'

def login(self):
    self.frame_1 = Frame(self.root, highlightbackground="#000000", borderwidth=0.01, highlightthickness=2)
    self.frame_1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

    self.img_fundo = PhotoImage(file="Imagens/login_fundo_1.png")
    self.img_cpf = PhotoImage(file="Imagens/login_textBox_1.png")
    self.img_senha = PhotoImage(file="Imagens/login_textBox_1.png")
    self.img_botao = PhotoImage(file="Imagens/login_botao_1.png")
    
    self.fundo = Label(self.frame_1, image= self.img_fundo)
    self.fundo.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

    self.root.title("login")
    self.atual_frame = self.frame_1
    
    #Criando Entradas

    #CPF
    self.fundo_cpf = Label(self.frame_1, image= self.img_cpf)
    self.fundo_cpf.place(relx= 0.6, rely = 0.3, relheight=0.12, relwidth=0.32)
    
    self.et_cpf = Entry(self.frame_1, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_cpf.place(relx= 0.615, rely = 0.316, relheight= 0.08, relwidth=0.285)
    self.et_cpf.focus()

    #senha
    self.label2 = Label(self.frame_1, image= self.img_senha)
    self.label2.place(relx= 0.6, rely = 0.48, relheight=0.12, relwidth=0.32)
    
    self.et_Senha = Entry(self.frame_1, show='*', bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Senha.place(relx= 0.615, rely = 0.495, relheight= 0.08, relwidth=0.285)
    
    #Criando os Botões
    self.bt_OK = Button(self.frame_1, text="OK", image= self.img_botao, borderwidth = 0, highlightthickness = 0, command = lambda: muda_tela_ator(self, gerenciador_BD.BD.verifica_senha(self, self.et_cpf.get(), self.et_Senha.get())))
    self.bt_OK.place(relx= 0.65, rely = 0.7, relheight= 0.11, relwidth=0.18)

def Estoquista(self, lista):
    self.FR_root_1 = Frame(self.root, background= "#ffffff", highlightbackground = "#000000", borderwidth=0.01, highlightthickness=2)
    self.FR_root_1.place(relx = 0.0, rely = 0.0, relheight = 1.0, relwidth= 0.346)
    
    self.img_fundo_funcionario = PhotoImage(file="Imagens/atores_fundo.png")
    self.img_logout = PhotoImage(file="Imagens/logout.png")
    
    self.fundo_estoquista = Label(self.FR_root_1, image= self.img_fundo_funcionario)
    self.fundo_estoquista.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=0.98)
    
    self.root.title("Estoquista")
    self.atual_frame = self.FR_root_1
    
    Cadastro_Produto(self)
    
    self.LB_nome = Label(self.FR_root_1, text = lista[1], background = fundo1, foreground=texto)
    self.LB_nome.place(relx = 0.3, rely = 0.11)

    self.LB_cpf_f = Label(self.FR_root_1, text = lista[2], background = fundo1, foreground=texto)
    self.LB_cpf_f.place(relx = 0.3, rely = 0.164)

    self.LB_cargo_f = Label(self.FR_root_1, text = lista[0], background = fundo1, foreground=texto)
    self.LB_cargo_f.place(relx = 0.3, rely = 0.225)
    
    self.LB_label1 = Label(self.FR_root_1, text = "Selecione a opção de Cadastro", background = fundo2, foreground=texto)
    self.LB_label1.place(relx = 0.02, rely = 0.325)
    
    self.lista_estoquista = ["Produto", "Pet"]
    self.value_inside = StringVar()
    self.value_inside.set(self.lista_estoquista[0])
    
    self.OP_Cadastro = OptionMenu(self.FR_root_1, self.value_inside, *self.lista_estoquista, command = lambda x: muda_frame_funcionalidade(self, self.value_inside.get()))
    self.OP_Cadastro.place(relx = 0.03, rely = 0.38)
    self.OP_Cadastro.config(background=option, highlightbackground = "#000000", foreground=texto)
    
    self.bt_OK = Button(self.FR_root_1 , text="Logout", image= self.img_logout, borderwidth = 0, highlightthickness = 0, command = lambda: Logout(self))
    self.bt_OK.place(relx= 0.4, rely = 0.89, relheight= 0.11, relwidth=0.55)

def Recepcionista(self, lista):
    self.FR_root_2 = Frame(self.root, background= fundo2, highlightbackground = "#000000", borderwidth=0.01, highlightthickness=2)
    self.FR_root_2.place(relx = 0.0, rely = 0.0, relheight = 1.0, relwidth= 0.346)
    
    self.img_fundo_funcionario = PhotoImage(file="Imagens/atores_fundo.png")
    self.img_logout = PhotoImage(file="Imagens/logout.png")
    
    self.fundo_recepcionista = Label(self.FR_root_2, image= self.img_fundo_funcionario)
    self.fundo_recepcionista.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=0.98)
    
    self.root.title("Recepcionista")
    self.atual_frame = self.FR_root_2
    
    Cadastro_Cliente(self)
    
    self.LB_nome = Label(self.FR_root_2, text = lista[1], background = fundo1, foreground=texto)
    self.LB_nome.place(relx = 0.3, rely = 0.11)
    
    self.LB_cpf_f = Label(self.FR_root_2, text = lista[2], background = fundo1, foreground=texto)
    self.LB_cpf_f.place(relx = 0.3, rely = 0.164)

    self.LB_cargo_f = Label(self.FR_root_2, text = lista[0], background = fundo1, foreground=texto)
    self.LB_cargo_f.place(relx = 0.3, rely = 0.225)
    
    self.LB_label1 = Label(self.FR_root_2, text = "Cadastros", background = fundo2)
    self.LB_label1.place(relx = 0.02, rely = 0.3)
    
    lista_recepcionista1 = ["Clientes"]
    self.value_inside1 = StringVar()
    self.value_inside1.set(lista_recepcionista1[0])
    
    self.OP_Cadastro = OptionMenu(self.FR_root_2, self.value_inside1, *lista_recepcionista1, command = lambda x:  muda_frame_funcionalidade(self, self.value_inside1.get()))
    self.OP_Cadastro.place(relx = 0.03, rely = 0.35)
    
    self.LB_label1 = Label(self.FR_root_2, text = "Vendas", background = fundo2)
    self.LB_label1.place(relx = 0.02, rely = 0.43)
    
    lista_recepcionista2 = ["Pets"]
    self.value_inside2 = StringVar()
    self.value_inside2.set(lista_recepcionista2[0])
    
    self.OP_Vendas = OptionMenu(self.FR_root_2, self.value_inside2, *lista_recepcionista2, command = lambda x:  muda_frame_funcionalidade(self, self.value_inside2.get()))
    self.OP_Vendas.place(relx = 0.03, rely = 0.48)
    
    self.bt_OK = Button(self.FR_root_2 , text="Logout", image= self.img_logout, borderwidth = 0, highlightthickness = 0, command = lambda: Logout(self))
    self.bt_OK.place(relx= 0.4, rely = 0.89, relheight= 0.11, relwidth=0.55)
    
def Caixa(self, lista):
    
    self.FR_root_3 = Frame(self.root, background= fundo2, highlightbackground = "#000000", borderwidth=0.01, highlightthickness=2)
    self.FR_root_3.place(relx = 0.0, rely = 0.0, relheight = 1.0, relwidth= 0.346)
    
    self.img_fundo_funcionario = PhotoImage(file="Imagens/atores_fundo.png")
    self.img_logout = PhotoImage(file="Imagens/logout.png")
    
    self.fundo_recepcionista = Label(self.FR_root_3, image= self.img_fundo_funcionario)
    self.fundo_recepcionista.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=0.98)
    
    self.root.title("Caixa")
    self.atual_frame = self.FR_root_3

    Vendas(self)

    self.LB_nome = Label(self.FR_root_3, text = lista[1], background = fundo1, foreground=texto)
    self.LB_nome.place(relx = 0.3, rely = 0.11)

    self.LB_cpf_f = Label(self.FR_root_3, text = lista[2], background = fundo1, foreground=texto)
    self.LB_cpf_f.place(relx = 0.3, rely = 0.164)

    self.LB_cargo_f = Label(self.FR_root_3, text = lista[0], background = fundo1, foreground=texto)
    self.LB_cargo_f.place(relx = 0.3, rely = 0.225)
    
    self.LB_label1 = Label(self.FR_root_3, text = "Vendas", background = fundo2)
    self.LB_label1.place(relx = 0.02, rely = 0.3)

    lista_caixa = ["Produtos"]
    self.value_inside = StringVar()
    self.value_inside.set(lista_caixa[0])
    self.OP_Vendas = OptionMenu(self.FR_root_3, self.value_inside, *lista_caixa, command = lambda x:  muda_frame_funcionalidade(self, self.value_inside.get()))
    self.OP_Vendas.place(relx = 0.03, rely = 0.35)

    self.bt_OK = Button(self.FR_root_3 , text="Logout", image= self.img_logout, borderwidth = 0, highlightthickness = 0, command = lambda: Logout(self))
    self.bt_OK.place(relx= 0.4, rely = 0.89, relheight= 0.11, relwidth=0.55)

def Cadastro_Produto(self):
    self.FR_root_ator_1 = Frame(self.root, background= fundo3, highlightbackground = '#000000', borderwidth=0.01, highlightthickness=2)
    self.FR_root_ator_1.place(relx = 0.337, rely = 0.0, relheight = 1.0, relwidth= 0.663)
    
    self.frame_funcionalidade = self.FR_root_ator_1

    self.LB_label1 = Label(self.FR_root_ator_1, text = "Cadastro Produtos", background = fundo3)
    self.LB_label1.pack()

def Cadastro_Pet(self):
    self.FR_root_ator_2 = Frame(self.root, background= fundo3, highlightbackground = "#000000", borderwidth=0.01, highlightthickness=2)
    self.FR_root_ator_2.place(relx = 0.337, rely = 0.0, relheight = 1.0, relwidth= 0.663)
    
    self.frame_funcionalidade = self.FR_root_ator_2

    self.LB_label1 = Label(self.FR_root_ator_2, text = "Cadastro Pet", background = fundo3)
    self.LB_label1.pack()
    
def Cadastro_Cliente(self):
    self.FR_root_ator_3 = Frame(self.root, background = fundo3, highlightbackground = "#000000", borderwidth=0.01, highlightthickness=2)
    self.FR_root_ator_3.place(relx = 0.337, rely = 0.0, relheight = 1.0, relwidth= 0.663)
    
    self.frame_funcionalidade = self.FR_root_ator_3

    self.LB_label1 = Label(self.FR_root_ator_3, text = "Cadastro Clientes", background = fundo3)
    self.LB_label1.pack()

def Vendas(self):
    self.FR_root_ator_4 = Frame(self.root, background = fundo3, highlightbackground = "#000000", borderwidth=0.01, highlightthickness=2)
    self.FR_root_ator_4.place(relx = 0.337, rely = 0.0, relheight = 1.0, relwidth= 0.663)
    
    self.frame_funcionalidade = self.FR_root_ator_4

    self.LB_label1 = Label(self.FR_root_ator_4, text = "Vendas", background = fundo3)
    self.LB_label1.pack()

def Venda_Pet(self):
    self.FR_root_ator_4 = Frame(self.root, background = fundo3, highlightbackground = "#000000", borderwidth=0.01, highlightthickness=2)
    self.FR_root_ator_4.place(relx = 0.337, rely = 0.0, relheight = 1.0, relwidth= 0.663)
    
    self.frame_funcionalidade = self.FR_root_ator_4

    self.LB_label1 = Label(self.FR_root_ator_4, text = "Venda Pet", background = fundo3)
    self.LB_label1.pack()

def muda_frame_funcionalidade(self, frame):
    if frame == "Produto":
        self.frame_funcionalidade.destroy()
        Cadastro_Produto(self)
    elif(frame == "Pet"):
        self.frame_funcionalidade.destroy()
        Cadastro_Pet(self)
    elif(frame == "Clientes"):
        self.frame_funcionalidade.destroy()
        Cadastro_Cliente(self)
    elif(frame == "Pets"):
        self.frame_funcionalidade.destroy()
        Venda_Pet(self)  
    elif(frame == "Produtos"):
        self.frame_funcionalidade.destroy()
        Vendas(self)   
        
def Logout(self):
    self.atual_frame.destroy()
    self.frame_funcionalidade.destroy()
    login(self)

def muda_tela_ator(self, lista):
    for i in lista:
            cargo = i[0]
    if lista == []:
        self.msgLimpar = messagebox.showerror('ERRO', 'Funcionário não encontrado. \n      Tente novamente.')
    elif(cargo == 'ESTOQUISTA'):
        self.atual_frame.destroy()  
        Estoquista(self, i)
    elif(cargo == 'RECEPCIONISTA'):
        self.atual_frame.destroy()  
        Recepcionista(self, i)
    elif(cargo == 'CAIXA'):
        self.atual_frame.destroy()
        Caixa(self, i)
        