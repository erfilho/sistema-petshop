# -*- coding: utf-8 -*-

from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import tkinter
from click import command

from numpy import complexfloating
import gerenciador_BD
import os
from pathlib import Path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

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

    self.img_fundo = PhotoImage(file= Path(ROOT_DIR, "img", "login_fundo_1.png"))
    self.img_cpf = PhotoImage(file= Path(ROOT_DIR, "img", "login_textBox_1.png"))
    self.img_senha = PhotoImage(file= Path(ROOT_DIR, "img", "login_textBox_1.png"))
    self.img_botao = PhotoImage(file= Path(ROOT_DIR, "img", "login_botao_1.png"))

    self.fundo = Label(self.frame_1, image= self.img_fundo)
    self.fundo.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
    
    # Adicionado ícone para a janela
    self.root.title("Petshop Mundocão - Login")
    self.root.iconphoto(False, PhotoImage(file= Path(ROOT_DIR, "img", "ico", "window_icon.png")))
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
    
    self.img_fundo_funcionario = PhotoImage(file= Path(ROOT_DIR, "img", "atores_fundo.png"))
    self.img_logout = PhotoImage(file= Path(ROOT_DIR, "img", "logout.png"))
    
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
    
    self.bt_logout = Button(self.FR_root_1 , text="Logout", image= self.img_logout, borderwidth = 0, highlightthickness = 0, command = lambda: Logout(self))
    self.bt_logout.place(relx= 0.4, rely = 0.89, relheight= 0.11, relwidth=0.55)

def Recepcionista(self, lista):
    self.FR_root_2 = Frame(self.root, background= fundo2, highlightbackground = "#000000", borderwidth=0.01, highlightthickness=2)
    self.FR_root_2.place(relx = 0.0, rely = 0.0, relheight = 1.0, relwidth= 0.346)
    
    self.img_fundo_funcionario = PhotoImage(file= Path(ROOT_DIR, "img", "atores_fundo.png"))
    self.img_logout = PhotoImage(file= Path(ROOT_DIR, "img", "logout.png"))
    
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
    
    lista_recepcionista1 = ["Clientes", "Pet"]
    self.value_inside1 = StringVar()
    self.value_inside1.set(lista_recepcionista1[0])
    
    self.OP_Cadastro = OptionMenu(self.FR_root_2, self.value_inside1, *lista_recepcionista1, command = lambda x:  muda_frame_funcionalidade(self, self.value_inside1.get()))
    self.OP_Cadastro.place(relx = 0.03, rely = 0.35)
    self.OP_Cadastro.config(background=option, highlightbackground = "#000000", foreground=texto)
    
    self.LB_label1 = Label(self.FR_root_2, text = "Vendas", background = fundo2)
    self.LB_label1.place(relx = 0.02, rely = 0.43)
    
    lista_recepcionista2 = ["Pets"]
    self.value_inside2 = StringVar()
    self.value_inside2.set(lista_recepcionista2[0])
    
    self.OP_Vendas = OptionMenu(self.FR_root_2, self.value_inside2, *lista_recepcionista2, command = lambda x:  muda_frame_funcionalidade(self, self.value_inside2.get()))
    self.OP_Vendas.place(relx = 0.03, rely = 0.48)
    self.OP_Vendas.config(background=option, highlightbackground = "#000000", foreground=texto)
    
    self.bt_logout = Button(self.FR_root_2 , text="Logout", image= self.img_logout, borderwidth = 0, highlightthickness = 0, command = lambda: Logout(self))
    self.bt_logout.place(relx= 0.4, rely = 0.89, relheight= 0.11, relwidth=0.55)
    
def Caixa(self, lista):
    
    self.FR_root_3 = Frame(self.root, background= fundo2, highlightbackground = "#000000", borderwidth=0.01, highlightthickness=2)
    self.FR_root_3.place(relx = 0.0, rely = 0.0, relheight = 1.0, relwidth= 0.346)
    
    self.img_fundo_funcionario = PhotoImage(file= Path(ROOT_DIR, "img", "atores_fundo.png"))
    self.img_logout = PhotoImage(file= Path(ROOT_DIR, "img", "logout.png"))
    
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
    self.OP_Vendas.config(background=option, highlightbackground = "#000000", foreground=texto)
    
    self.bt_logout = Button(self.FR_root_3 , text="Logout", image= self.img_logout, borderwidth = 0, highlightthickness = 0, command = lambda: Logout(self))
    self.bt_logout.place(relx= 0.4, rely = 0.89, relheight= 0.11, relwidth=0.55)

# Added by Erineldo 26/05 
# Função que vai limpar os campos de entrada do cadastro de produtos
def limpa_campos_produtos(self):
    self.et_Codigo.delete(0, 'end')
    self.et_Nome.delete(0, 'end')
    self.et_Preco.delete(0, 'end')

def Cadastro_Produto(self):
    self.FR_root_ator_1 = Frame(self.root, background= fundo3, highlightbackground = '#000000', borderwidth=0.01, highlightthickness=2)
    self.FR_root_ator_1.place(relx = 0.337, rely = 0.0, relheight = 1.0, relwidth= 0.663)
    
    self.LB_label1 = Label(self.FR_root_ator_1, text = "Cadastro Produtos", background = fundo3)
    self.LB_label1.pack()   
    self.frame_funcionalidade = self.FR_root_ator_1
    
    self.img_fundo = PhotoImage(file= Path(ROOT_DIR, "img", "fundo_entry_cadastro.png"))
    self.img_bt_salvar = PhotoImage(file= Path(ROOT_DIR, "img", "botao_salvar.png"))
    self.img_bt_cancelar = PhotoImage(file= Path(ROOT_DIR, "img", "botao_cancelar.png"))
    self.img_bt_limpar = PhotoImage(file= Path(ROOT_DIR, "img", "botao_limpar.png"))
    
    #entradas
    #codigo do produto
    #label
    self.fundo_Codigo = Label(self.FR_root_ator_1, text="Código do Produto", font=fonte, background=fundo3)
    self.fundo_Codigo.place(relx= 0.1, rely = 0.1)
    #imagem de fundo
    self.fundo_Codigo = Label(self.FR_root_ator_1, image= self.img_fundo)
    self.fundo_Codigo.place(relx= 0.05, rely = 0.15, relheight=0.115, relwidth=0.46)
    #entry
    # Mod by Erineldo - Nome não compatível
    self.et_Codigo = Entry(self.FR_root_ator_1, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Codigo.place(relx= 0.065, rely = 0.165, relheight= 0.075, relwidth=0.43)
    self.et_Codigo.focus()
    
    #nome do produto
    #label
    self.fundo_Nome = Label(self.FR_root_ator_1, text="Nome do Produto", font=fonte, background=fundo3)
    self.fundo_Nome.place(relx= 0.1, rely = 0.3)
    #imagem de fundo
    self.fundo_Nome = Label(self.FR_root_ator_1, image= self.img_fundo)
    self.fundo_Nome.place(relx= 0.05, rely = 0.35, relheight=0.115, relwidth=0.46)
    #entry
    self.et_Nome = Entry(self.FR_root_ator_1, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Nome.place(relx= 0.065, rely = 0.365, relheight= 0.075, relwidth=0.43)
    
    #nome do produto
    #label
    self.fundo_Preco = Label(self.FR_root_ator_1, text="Preço do Produto", font=fonte, background=fundo3)
    self.fundo_Preco.place(relx= 0.1, rely = 0.5)
    #imagem de fundo
    self.fundo_Preco = Label(self.FR_root_ator_1, image= self.img_fundo)
    self.fundo_Preco.place(relx= 0.05, rely = 0.55, relheight=0.115, relwidth=0.46)
    #entry
    self.et_Preco = Entry(self.FR_root_ator_1, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Preco.place(relx= 0.065, rely = 0.565, relheight= 0.075, relwidth=0.43)
    
    #Botões
    #Salvar
    # Mod by Erineldo - Added cadastro produto
    self.bt_salvar = Button(self.FR_root_ator_1, image= self.img_bt_salvar, borderwidth = 0, highlightthickness = 0, command= lambda: gerenciador_BD.BD.cad_produto(self, self.et_Codigo.get(), self.et_Nome.get(), self.et_Preco.get()))
    self.bt_salvar.place(relx= 0.65, rely = 0.86, relheight= 0.13, relwidth=0.32)
    
    #Cancelar
    # Mod by Erineldo - Nomes de botões iguais
    self.bt_cancelar = Button(self.FR_root_ator_1, image= self.img_bt_cancelar, borderwidth = 0, highlightthickness = 0)
    self.bt_cancelar.place(relx= 0.34, rely = 0.86, relheight= 0.13, relwidth=0.32)
    
    #Limpar
    # Mod by Erineldo - Nomes de botões iguais
    self.bt_limpar = Button(self.FR_root_ator_1, image= self.img_bt_limpar, borderwidth = 0, highlightthickness = 0, command= lambda: limpa_campos_produtos(self))
    self.bt_limpar.place(relx= 0.02, rely = 0.86, relheight= 0.13, relwidth=0.32) 

# Added by Erineldo 26/05
# Função que vai limpar os campos de entrada dos campos de clientes
def limpa_campos_pet(self):
    self.et_Codigo.delete(0, 'end')
    self.et_Nome.delete(0, 'end')
    self.et_Idade.delete(0, 'end')
    self.et_Sexo.delete(0, 'end')
    self.et_Codigo_Dono.delete(0, 'end')
    self.et_Raca.delete(0, 'end')
    self.et_Preco.delete(0, 'end')
    self.CB_pet_para_venda.deselect()

def Cadastro_Pet(self):
    self.FR_root_ator_2 = Frame(self.root, background= fundo3, highlightbackground = "#000000", borderwidth=0.01, highlightthickness=2)
    self.FR_root_ator_2.place(relx = 0.337, rely = 0.0, relheight = 1.0, relwidth= 0.663)
    
    self.LB_label1 = Label(self.FR_root_ator_2, text = "Cadastro Pets", background = fundo3)
    self.LB_label1.pack()
    
    self.frame_funcionalidade = self.FR_root_ator_2

    self.img_fundo = PhotoImage(file= Path(ROOT_DIR, "img", "fundo_entry_cadastro.png"))
    self.img_fundo2 = PhotoImage(file= Path(ROOT_DIR, "img", "fundo_entry_cadastro_P.png"))
    self.img_bt_salvar = PhotoImage(file= Path(ROOT_DIR, "img", "botao_salvar.png"))
    self.img_bt_cancelar = PhotoImage(file= Path(ROOT_DIR, "img", "botao_cancelar.png"))
    self.img_bt_limpar = PhotoImage(file= Path(ROOT_DIR, "img", "botao_limpar.png"))
    
    #entradas
    #codigo do pet
    #label
    self.fundo_Codigo = Label(self.FR_root_ator_2, text="Código do Pet", font=fonte, background=fundo3)
    self.fundo_Codigo.place(relx= 0.1, rely = 0.05)
    #imagem de fundo
    self.fundo_Codigo = Label(self.FR_root_ator_2, image= self.img_fundo)
    self.fundo_Codigo.place(relx= 0.05, rely = 0.1, relheight=0.115, relwidth=0.46)
    #entry
    self.et_Codigo = Entry(self.FR_root_ator_2, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Codigo.place(relx= 0.065, rely = 0.115, relheight= 0.075, relwidth=0.43)
    self.et_Codigo.focus()
    
    #nome do pet
    #label
    self.fundo_Nome = Label(self.FR_root_ator_2, text="Nome do Pet", font=fonte, background=fundo3)
    self.fundo_Nome.place(relx= 0.1, rely = 0.21)
    #imagem de fundo
    self.fundo_Nome = Label(self.FR_root_ator_2, image= self.img_fundo)
    self.fundo_Nome.place(relx= 0.05, rely = 0.25, relheight=0.115, relwidth=0.46)
    #entry
    self.et_Nome = Entry(self.FR_root_ator_2, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Nome.place(relx= 0.065, rely = 0.265, relheight= 0.075, relwidth=0.43)
    
    #idade do pet
    #label
    self.fundo_Idade = Label(self.FR_root_ator_2, text="Idade do Pet", font=fonte, background=fundo3)
    self.fundo_Idade.place(relx= 0.1, rely = 0.355)
    #imagem de fundo
    self.fundo_Idade = Label(self.FR_root_ator_2, image= self.img_fundo)
    self.fundo_Idade.place(relx= 0.05, rely = 0.4, relheight=0.115, relwidth=0.46)
    #entry
    self.et_Idade = Entry(self.FR_root_ator_2, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Idade.place(relx= 0.065, rely = 0.415, relheight= 0.075, relwidth=0.43)
    
    #Sexo
    #label
    self.fundo_Sexo = Label(self.FR_root_ator_2, text="Sexo", font=fonte, background=fundo3)
    self.fundo_Sexo.place(relx= 0.1, rely = 0.52)
    #imagem de fundo
    self.fundo_Sexo = Label(self.FR_root_ator_2, image= self.img_fundo2)
    self.fundo_Sexo.place(relx= 0.05, rely = 0.57, relheight=0.11, relwidth=0.21)
    #entry
    self.et_Sexo = Entry(self.FR_root_ator_2, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Sexo.place(relx= 0.065, rely = 0.585, relheight= 0.075, relwidth=0.185)
    
    #Codigo dono
    #label
    self.fundo_Codigo_Dono = Label(self.FR_root_ator_2, text="Código do Dono", font=fonte, background=fundo3)
    self.fundo_Codigo_Dono.place(relx= 0.4, rely = 0.52)
    #imagem de fundo
    self.fundo_Codigo_Dono = Label(self.FR_root_ator_2, image= self.img_fundo)
    self.fundo_Codigo_Dono.place(relx= 0.37, rely = 0.57, relheight=0.115, relwidth=0.46)
    #entry
    self.et_Codigo_Dono = Entry(self.FR_root_ator_2, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Codigo_Dono.place(relx= 0.385, rely = 0.585, relheight= 0.075, relwidth=0.43)
    
    #Raça
    #label
    self.fundo_Raca = Label(self.FR_root_ator_2, text="Raça", font=fonte, background=fundo3)
    self.fundo_Raca.place(relx= 0.1, rely = 0.68)
    #imagem de fundo
    self.fundo_Raca = Label(self.FR_root_ator_2, image= self.img_fundo2)
    self.fundo_Raca.place(relx= 0.05, rely = 0.72, relheight=0.11, relwidth=0.21)
    #entry
    self.et_Raca = Entry(self.FR_root_ator_2, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Raca.place(relx= 0.065, rely = 0.733, relheight= 0.075, relwidth=0.185)
    
    #Preço
    #label
    self.fundo_Preco = Label(self.FR_root_ator_2, text="Preço", font=fonte, background=fundo3)
    self.fundo_Preco.place(relx= 0.4, rely = 0.68)
    #imagem de fundo
    self.fundo_Preco = Label(self.FR_root_ator_2, image= self.img_fundo2)
    self.fundo_Preco.place(relx= 0.37, rely = 0.72, relheight=0.11, relwidth=0.21)
    #entry
    self.et_Preco = Entry(self.FR_root_ator_2, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Preco.place(relx= 0.39, rely = 0.733, relheight= 0.075, relwidth=0.185)
    
    #checkButton
    self.valor_Checkbox = tkinter.IntVar()
    self.CB_pet_para_venda = Checkbutton(self.FR_root_ator_2, variable= self.valor_Checkbox, text= 'Pet para Venda', onvalue= 1 , offvalue= 0, background=fundo3, highlightbackground = fundo3)
    self.CB_pet_para_venda.place(relx= 0.6, rely = 0.28)

    #Botões
    #Salvar
    self.bt_salvar = Button(self.FR_root_ator_2, image= self.img_bt_salvar, borderwidth = 0, highlightthickness = 0, command= lambda: gerenciador_BD.BD.cad_pet(self, self.et_Codigo.get(), self.et_Nome.get(), self.et_Idade.get(), self.et_Sexo.get(), self.et_Codigo_Dono.get(), self.et_Raca.get(), self.et_Preco.get(), self.valor_Checkbox.get()))
    self.bt_salvar.place(relx= 0.65, rely = 0.86, relheight= 0.13, relwidth=0.32)
    
    #Cancelar
    self.bt_cancelar = Button(self.FR_root_ator_2, image= self.img_bt_cancelar, borderwidth = 0, highlightthickness = 0)
    self.bt_cancelar.place(relx= 0.34, rely = 0.86, relheight= 0.13, relwidth=0.32)
    
    #Limpar
    self.bt_limpar = Button(self.FR_root_ator_2, image= self.img_bt_limpar, borderwidth = 0, highlightthickness = 0, command= lambda: limpa_campos_pet(self))
    self.bt_limpar.place(relx= 0.02, rely = 0.86, relheight= 0.13, relwidth=0.32)

# Added by Erineldo 26/05
# Função que limpa os campos de entrada de dados no cadastro de clientes
def limpa_campos_clientes(self):
    self.et_Codigo.delete(0, 'end')
    self.et_Nome.delete(0, 'end')
    self.et_CPF.delete(0, 'end')
    self.et_Data_nascimento.delete(0, 'end')
    self.et_Logradouro.delete(0, 'end')
    self.et_Cidade.delete(0, 'end')
    self.et_Bairro.delete(0, 'end')
    self.et_UF.delete(0, 'end')
    self.et_Celular.delete(0, 'end')
    self.et_Email.delete(0, 'end')

def limpa_campos_vendaPet_CODPet(self):
    self.et_Codigo_pet.delete(0, 'end')
def limpa_campos_vendaPet_CODDono(self):
    self.et_Codigo_dono.delete(0, 'end')
def limpa_campos_vendaPet(self):
    self.et_Codigo_venda_pet.delete(0, 'end')
    limpa_campos_vendaPet_CODPet(self)
    limpa_campos_vendaPet_CODDono(self)

def Cadastro_Cliente(self):
    self.FR_root_ator_3 = Frame(self.root, background = fundo3, highlightbackground = "#000000", borderwidth=0.01, highlightthickness=2)
    self.FR_root_ator_3.place(relx = 0.337, rely = 0.0, relheight = 1.0, relwidth= 0.663)
    
    self.LB_label1 = Label(self.FR_root_ator_3, text = "Cadastro Clientes", background = fundo3)
    self.LB_label1.pack()
    
    self.frame_funcionalidade = self.FR_root_ator_3

    self.img_fundo = PhotoImage(file= Path(ROOT_DIR, "img", "fundo_entry_cadastro.png"))
    self.img_fundo2 = PhotoImage(file= Path(ROOT_DIR, "img", "fundo_entry_cadastro_P.png"))
    self.img_bt_salvar = PhotoImage(file= Path(ROOT_DIR, "img", "botao_salvar.png"))
    self.img_bt_cancelar = PhotoImage(file= Path(ROOT_DIR, "img", "botao_cancelar.png"))
    self.img_bt_limpar = PhotoImage(file= Path(ROOT_DIR, "img", "botao_limpar.png"))


    #entradas
    #codigo do Cliente
    #label
    self.label_Codigo = Label(self.FR_root_ator_3, text="Código", font=fonte, background=fundo3)
    self.label_Codigo.place(relx= 0.1, rely = 0.05)
    #imagem de fundo
    self.fundo_Codigo = Label(self.FR_root_ator_3, image= self.img_fundo)
    self.fundo_Codigo.place(relx= 0.05, rely = 0.1, relheight=0.115, relwidth=0.46)
    #entry
    self.et_Codigo = Entry(self.FR_root_ator_3, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Codigo.place(relx= 0.065, rely = 0.115, relheight= 0.075, relwidth=0.43)
    self.et_Codigo.focus()
    

    #nome do Cliente
    #label
    self.label_Nome = Label(self.FR_root_ator_3, text="Nome", font=fonte, background=fundo3)
    self.label_Nome.place(relx= 0.1, rely = 0.21)
    #imagem de fundo
    self.fundo_Nome = Label(self.FR_root_ator_3, image= self.img_fundo)
    self.fundo_Nome.place(relx= 0.05, rely = 0.25, relheight=0.115, relwidth=0.46)
    #entry
    self.et_Nome = Entry(self.FR_root_ator_3, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Nome.place(relx= 0.065, rely = 0.265, relheight= 0.075, relwidth=0.43)
    
    #cpf do Cliente
    #label
    self.label_CPF = Label(self.FR_root_ator_3, text="CPF", font=fonte, background=fundo3)
    self.label_CPF.place(relx= 0.1, rely = 0.355)
    #imagem de fundo
    self.fundo_CPF = Label(self.FR_root_ator_3, image= self.img_fundo)
    self.fundo_CPF.place(relx= 0.05, rely = 0.4, relheight=0.115, relwidth=0.46)
    #entry
    self.et_CPF = Entry(self.FR_root_ator_3, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_CPF.place(relx= 0.065, rely = 0.415, relheight= 0.075, relwidth=0.43)

    #data de nascimento do Cliente
    #label
    self.label_data_nascimento = Label(self.FR_root_ator_3, text="Data de Nascimento", font=fonte, background=fundo3)
    self.label_data_nascimento.place(relx= 0.1, rely = 0.52)
    #imagem de fundo
    self.fundo_data_nascimento = Label(self.FR_root_ator_3, image= self.img_fundo)
    self.fundo_data_nascimento.place(relx= 0.05, rely = 0.57, relheight=0.115, relwidth=0.46)
    #entry
    self.et_Data_nascimento = Entry(self.FR_root_ator_3, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Data_nascimento.place(relx= 0.065, rely = 0.585, relheight= 0.075, relwidth=0.43)
      
    #Logradouro
    #label
    self.label_Logradouro = Label(self.FR_root_ator_3, text="Logradouro", font=fonte, background=fundo3)
    self.label_Logradouro.place(relx= 0.1, rely = 0.68)
    #imagem de fundo
    self.fundo_Logradouro = Label(self.FR_root_ator_3, image= self.img_fundo)
    self.fundo_Logradouro.place(relx= 0.05, rely = 0.72, relheight=0.115, relwidth=0.46)
    #entry
    self.et_Logradouro = Entry(self.FR_root_ator_3, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Logradouro.place(relx= 0.065, rely = 0.733, relheight= 0.075, relwidth=0.43)
    
    #Cidade
    #label
    self.label_Cidade = Label(self.FR_root_ator_3, text="Cidade", font=fonte, background=fundo3)
    self.label_Cidade.place(relx= 0.6, rely = 0.05)
    #imagem de fundo
    self.fundo_Cidade = Label(self.FR_root_ator_3, image= self.img_fundo)
    self.fundo_Cidade.place(relx= 0.53, rely = 0.1, relheight=0.115, relwidth=0.46)
    #entry
    self.et_Cidade = Entry(self.FR_root_ator_3, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Cidade.place(relx= 0.545, rely = 0.115, relheight= 0.075, relwidth=0.43)
    
    #Bairro
    #label
    self.label_Bairro = Label(self.FR_root_ator_3, text="Bairro", font=fonte, background=fundo3)
    self.label_Bairro.place(relx= 0.6, rely = 0.21)
    #imagem de fundo
    self.fundo_Bairro = Label(self.FR_root_ator_3, image= self.img_fundo)
    self.fundo_Bairro.place(relx= 0.53, rely = 0.25, relheight=0.115, relwidth=0.46)
    #entry
    self.et_Bairro = Entry(self.FR_root_ator_3, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Bairro.place(relx= 0.545, rely = 0.265, relheight= 0.075, relwidth=0.43)
    
    #UF
    #label
    self.label_UF = Label(self.FR_root_ator_3, text="UF", font=fonte, background=fundo3)
    self.label_UF.place(relx= 0.6, rely = 0.355)
    #imagem de fundo
    self.fundo_UF = Label(self.FR_root_ator_3, image= self.img_fundo2)
    self.fundo_UF.place(relx= 0.53, rely = 0.4, relheight=0.11, relwidth=0.21)
    #entry
    self.et_UF = Entry(self.FR_root_ator_3, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_UF.place(relx= 0.545, rely = 0.415, relheight= 0.075, relwidth=0.185)
    
    #Celular
    #label
    self.label_Celular = Label(self.FR_root_ator_3, text="Celular", font=fonte, background=fundo3)
    self.label_Celular.place(relx= 0.6, rely = 0.52)
    #imagem de fundo
    self.fundo_Celular = Label(self.FR_root_ator_3, image= self.img_fundo)
    self.fundo_Celular.place(relx= 0.53, rely = 0.57, relheight=0.115, relwidth=0.46)
    #entry
    self.et_Celular = Entry(self.FR_root_ator_3, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Celular.place(relx= 0.545, rely = 0.585, relheight= 0.075, relwidth=0.43)
    
    #email
    #label
    self.label_Email = Label(self.FR_root_ator_3, text="E-Mail", font=fonte, background=fundo3)
    self.label_Email.place(relx= 0.6, rely = 0.68)
    #imagem de fundo
    self.fundo_Email = Label(self.FR_root_ator_3, image= self.img_fundo)
    self.fundo_Email.place(relx= 0.53, rely = 0.72, relheight=0.115, relwidth=0.46)
    #entry
    self.et_Email = Entry(self.FR_root_ator_3, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Email.place(relx= 0.545, rely = 0.735, relheight= 0.075, relwidth=0.43)
    
    #Botões
    #Salvar
    self.bt_salvar = Button(self.FR_root_ator_3, image= self.img_bt_salvar, borderwidth = 0, highlightthickness = 0, command= lambda: gerenciador_BD.BD.cad_cliente(self, self.et_Codigo.get(), self.et_Nome.get(), self.et_CPF.get(), self.et_Data_nascimento.get(), self.et_Logradouro.get(), self.et_Cidade.get(), self.et_Bairro.get(), self.et_UF.get(), self.et_Celular.get(), self.et_Email.get()))
    self.bt_salvar.place(relx= 0.65, rely = 0.86, relheight= 0.13, relwidth=0.32)
    
    #Cancelar
    self.bt_cancelar = Button(self.FR_root_ator_3, image= self.img_bt_cancelar, borderwidth = 0, highlightthickness = 0)
    self.bt_cancelar.place(relx= 0.34, rely = 0.86, relheight= 0.13, relwidth=0.32)
    
    #Limpar
    self.bt_limpar = Button(self.FR_root_ator_3, image= self.img_bt_limpar, borderwidth = 0, highlightthickness = 0, command= lambda: limpa_campos_clientes(self))
    self.bt_limpar.place(relx= 0.02, rely = 0.86, relheight= 0.13, relwidth=0.32)
def Venda_Pet(self):
    self.FR_root_ator_4 = Frame(self.root, background = fundo3, highlightbackground = "#000000", borderwidth=0.01, highlightthickness=2)
    self.FR_root_ator_4.place(relx = 0.337, rely = 0.0, relheight = 1.0, relwidth= 0.663)
    
    self.LB_label1 = Label(self.FR_root_ator_4, text = "Venda Pet", background = fundo3)
    self.LB_label1.pack()
    
    self.frame_funcionalidade = self.FR_root_ator_4

    self.img_fundo = PhotoImage(file= Path(ROOT_DIR, "img", "fundo_entry_cadastro_P.png"))
    self.img_bt_salvar = PhotoImage(file= Path(ROOT_DIR, "img", "botao_salvar.png"))
    self.img_bt_cancelar = PhotoImage(file= Path(ROOT_DIR, "img", "botao_cancelar.png"))
    self.img_bt_limpar = PhotoImage(file= Path(ROOT_DIR, "img", "botao_limpar.png"))
    self.img_bt_encomenda = PhotoImage(file= Path(ROOT_DIR, "img", "botao_encomenda.png"))
    
    #entradas
    #codigo do Cliente
    #label
    self.label_Codigo_pet = Label(self.FR_root_ator_4, text="Código do Pet", font=fonte, background=fundo3)
    self.label_Codigo_pet.place(relx= 0.05, rely = 0.05)
    #imagem de fundo
    self.fundo_Codigo_pet = Label(self.FR_root_ator_4, image= self.img_fundo)
    self.fundo_Codigo_pet.place(relx= 0.05, rely = 0.1, relheight=0.11, relwidth=0.21)
    #entry
    self.et_Codigo_pet = Entry(self.FR_root_ator_4, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Codigo_pet.place(relx= 0.065, rely = 0.115, relheight= 0.075, relwidth=0.185)
    self.et_Codigo_pet.focus()
    #bind da Entry
    self.et_Codigo_pet.bind('<FocusIn>',lista_pets_venda(self))
    self.et_Codigo_pet.bind('<Button-1>', lambda x: muda_lista_venda_pet(self, "COD-PET"))
        
    #label
    self.label_Codigo_dono = Label(self.FR_root_ator_4, text="Código do Dono", font=fonte, background=fundo3)
    self.label_Codigo_dono.place(relx= 0.05, rely = 0.21)
    #imagem de fundo
    self.fundo_Codigo_dono = Label(self.FR_root_ator_4, image= self.img_fundo)
    self.fundo_Codigo_dono.place(relx= 0.05, rely = 0.25, relheight=0.11, relwidth=0.21)
    #entry
    self.et_Codigo_dono = Entry(self.FR_root_ator_4, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Codigo_dono.place(relx= 0.065, rely = 0.265, relheight= 0.075, relwidth=0.185)
    #bind da entry
    self.et_Codigo_dono.bind('<Button-1>', lambda x: muda_lista_venda_pet(self, "COD-DONO"))
    
    #label
    self.label_Codigo_venda_pet = Label(self.FR_root_ator_4, text="Código de Venda", font=fonte, background=fundo3)
    self.label_Codigo_venda_pet.place(relx= 0.02, rely = 0.355)
    #imagem de fundo
    self.fundo_Codigo_venda_pet = Label(self.FR_root_ator_4, image= self.img_fundo)
    self.fundo_Codigo_venda_pet.place(relx= 0.05, rely = 0.4, relheight=0.11, relwidth=0.21)
    #entry
    self.et_Codigo_venda_pet = Entry(self.FR_root_ator_4, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Codigo_venda_pet.place(relx= 0.065, rely = 0.415, relheight= 0.075, relwidth=0.185)   
    #bind da entry
    self.et_Codigo_venda_pet.bind('<Button-1>',lambda x: muda_lista_venda_pet(self, "NA"))
    
    #Botões
    #Salvar
    self.bt_salvar = Button(self.FR_root_ator_4, image= self.img_bt_salvar, borderwidth = 0, highlightthickness = 0)
    self.bt_salvar.place(relx= 0.65, rely = 0.86, relheight= 0.13, relwidth=0.32)
    
    #Cancelar
    self.bt_cancelar = Button(self.FR_root_ator_4, image= self.img_bt_cancelar, borderwidth = 0, highlightthickness = 0, command= lambda: gerenciador_BD.BD.teste_Clientes(self))
    self.bt_cancelar.place(relx= 0.34, rely = 0.86, relheight= 0.13, relwidth=0.32)
    
    #Limpar
    self.bt_limpar = Button(self.FR_root_ator_4, image= self.img_bt_limpar, borderwidth = 0, highlightthickness = 0, command= lambda : limpa_campos_vendaPet(self))
    self.bt_limpar.place(relx= 0.02, rely = 0.86, relheight= 0.13, relwidth=0.32)
    
    #Encomendar Pet
    self.bt_reservar = Button(self.FR_root_ator_4, image= self.img_bt_encomenda, borderwidth = 0, highlightthickness = 0, command= lambda: muda_frame_funcionalidade(self, "Encomenda"))
    self.bt_reservar.place(relx= 0.02, rely = 0.7, relheight= 0.115, relwidth=0.28)
    
def Encomenda_Pet(self):
    self.FR_root_ator_4 = Frame(self.root, background = fundo3, highlightbackground = "#000000", borderwidth=0.01, highlightthickness=2)
    self.FR_root_ator_4.place(relx = 0.337, rely = 0.0, relheight = 1.0, relwidth= 0.663)
    self.LB_label1 = Label(self.FR_root_ator_4, text = "Encomeda de Pet", background = fundo3)
    self.LB_label1.pack()
    
    self.frame_funcionalidade = self.FR_root_ator_4

    self.img_fundo = PhotoImage(file= Path(ROOT_DIR, "img", "fundo_entry_cadastro.png"))
    self.img_bt_salvar = PhotoImage(file= Path(ROOT_DIR, "img", "botao_salvar.png"))
    self.img_bt_cancelar = PhotoImage(file= Path(ROOT_DIR, "img", "botao_cancelar.png"))
    self.img_bt_limpar = PhotoImage(file= Path(ROOT_DIR, "img", "botao_limpar.png"))
    
    #entradas
    
    #codigo encomenda
    #label
    self.label_codigo_encomenda = Label(self.FR_root_ator_4, text="Código de encomenda Pet", font=fonte, background=fundo3)
    self.label_codigo_encomenda.place(relx= 0.1, rely = 0.05)
    #imagem de fundo
    self.fundo_codigo_encomenda  = Label(self.FR_root_ator_4, image= self.img_fundo)
    self.fundo_codigo_encomenda.place(relx= 0.05, rely = 0.1, relheight=0.115, relwidth=0.46)
    #entry
    self.et_Codigo_encomenda = Entry(self.FR_root_ator_4, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Codigo_encomenda .place(relx= 0.065, rely = 0.115, relheight= 0.075, relwidth=0.43)
    
    #Codigo do Cliente
    #label
    self.label_Codigo_cli = Label(self.FR_root_ator_4, text="Código do Cliente", font=fonte, background=fundo3)
    self.label_Codigo_cli.place(relx= 0.1, rely = 0.21)
    #imagem de fundo
    self.fundo_Codigo_cli = Label(self.FR_root_ator_4, image= self.img_fundo)
    self.fundo_Codigo_cli.place(relx= 0.05, rely = 0.25, relheight=0.115, relwidth=0.46)
    #entry
    self.et_Codigo_cli = Entry(self.FR_root_ator_4, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Codigo_cli.place(relx= 0.065, rely = 0.265, relheight= 0.075, relwidth=0.43)

    #raca desejada
    #label
    self.label_raca = Label(self.FR_root_ator_4, text="Raça Desejada", font=fonte, background=fundo3)
    self.label_raca.place(relx= 0.1, rely = 0.355)
    #imagem de fundo
    self.fundo_raca = Label(self.FR_root_ator_4, image= self.img_fundo)
    self.fundo_raca.place(relx= 0.05, rely = 0.4, relheight=0.115, relwidth=0.46)
    #entry
    self.et_raca = Entry(self.FR_root_ator_4, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_raca.place(relx= 0.065, rely = 0.415, relheight= 0.075, relwidth=0.43)

    #Sexo desejado
    #label
    self.label_sexo = Label(self.FR_root_ator_4, text="Sexo Desejado", font=fonte, background=fundo3)
    self.label_sexo.place(relx= 0.1, rely = 0.52)
    #imagem de fundo
    self.fundo_sexo = Label(self.FR_root_ator_4, image= self.img_fundo)
    self.fundo_sexo.place(relx= 0.05, rely = 0.57, relheight=0.115, relwidth=0.46)
    #entry
    self.et_sexo = Entry(self.FR_root_ator_4, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_sexo.place(relx= 0.065, rely = 0.585, relheight= 0.075, relwidth=0.43)
      
    #Idade maxima
    #label
    self.label_idade = Label(self.FR_root_ator_4, text="Idade máxima", font=fonte, background=fundo3)
    self.label_idade.place(relx= 0.1, rely = 0.68)
    #imagem de fundo
    self.fundo_idade = Label(self.FR_root_ator_4, image= self.img_fundo)
    self.fundo_idade.place(relx= 0.05, rely = 0.72, relheight=0.115, relwidth=0.46)
    #entry
    self.et_idade = Entry(self.FR_root_ator_4, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_idade.place(relx= 0.065, rely = 0.733, relheight= 0.075, relwidth=0.43)
    
    #Valor Maximo
    #label
    self.label_valor = Label(self.FR_root_ator_4, text="Valor Máximo", font=fonte, background=fundo3)
    self.label_valor.place(relx= 0.6, rely = 0.05)
    #imagem de fundo
    self.fundo_valor = Label(self.FR_root_ator_4, image= self.img_fundo)
    self.fundo_valor.place(relx= 0.53, rely = 0.1, relheight=0.115, relwidth=0.46)
    #entry
    self.et_valor = Entry(self.FR_root_ator_4, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_valor.place(relx= 0.545, rely = 0.115, relheight= 0.075, relwidth=0.43)
    
    #codigo pet
    #label
    self.label_codigo_pet = Label(self.FR_root_ator_4, text="Código do Pet", font=fonte, background=fundo3)
    self.label_codigo_pet.place(relx= 0.6, rely = 0.21)
    #imagem de fundo
    self.fundo_codigo_pet = Label(self.FR_root_ator_4, image= self.img_fundo)
    self.fundo_codigo_pet.place(relx= 0.53, rely = 0.25, relheight=0.115, relwidth=0.46)
    #entry
    self.et_Codigo_pet = Entry(self.FR_root_ator_4, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Codigo_pet.place(relx= 0.545, rely = 0.265, relheight= 0.075, relwidth=0.43)

    #Botões
    #Salvar
    self.bt_salvar = Button(self.FR_root_ator_4, image= self.img_bt_salvar, borderwidth = 0, highlightthickness = 0)
    self.bt_salvar.place(relx= 0.65, rely = 0.86, relheight= 0.13, relwidth=0.32)
    
    #Cancelar
    self.bt_cancelar = Button(self.FR_root_ator_4, image= self.img_bt_cancelar, borderwidth = 0, highlightthickness = 0,command= lambda: muda_frame_funcionalidade(self, "Pets"))
    self.bt_cancelar.place(relx= 0.34, rely = 0.86, relheight= 0.13, relwidth=0.32)
    
    #Limpar
    self.bt_limpar = Button(self.FR_root_ator_4, image= self.img_bt_limpar, borderwidth = 0, highlightthickness = 0)
    self.bt_limpar.place(relx= 0.02, rely = 0.86, relheight= 0.13, relwidth=0.32)

def Vendas(self):
    self.FR_root_ator_5 = Frame(self.root, background = fundo3, highlightbackground = "#000000", borderwidth=0.01, highlightthickness=2)
    self.FR_root_ator_5.place(relx = 0.337, rely = 0.0, relheight = 1.0, relwidth= 0.663)
    
    self.FR_lista_compra = Frame(self.FR_root_ator_5, background = "#ffffff", highlightbackground = "#000000", borderwidth=0.01, highlightthickness=2)
    self.FR_lista_compra.place(relx = 0.01, rely = 0.25, relheight = 0.6, relwidth= 0.98)
    
    self.LB_label1 = Label(self.FR_root_ator_5, text = "Vendas", background = fundo3)
    self.LB_label1.pack()
    
    self.frame_funcionalidade = self.FR_root_ator_5
    
    self.img_fundo = PhotoImage(file= Path(ROOT_DIR, "img", "fundo_entry_cadastro_P.png"))
    self.img_bt_finalizar = PhotoImage(file= Path(ROOT_DIR, "img", "botao_finalizar.png"))
    self.img_bt_cancelar = PhotoImage(file= Path(ROOT_DIR, "img", "botao_cancelar.png"))
    self.img_bt_limpar = PhotoImage(file= Path(ROOT_DIR, "img", "botao_limpar.png"))
    self.img_bt_adicionar = PhotoImage(file= Path(ROOT_DIR, "img", "botao_adicionar.png"))
    
    #entradas
    #codigo do Produto
    #label
    self.label_Codigo_produto = Label(self.FR_root_ator_5, text="Código do Produto", font=(fonte, 10), background=fundo3)
    self.label_Codigo_produto.place(relx= 0.02, rely = 0.05)
    #imagem de fundo
    self.fundo_Codigo_produto = Label(self.FR_root_ator_5, image= self.img_fundo)
    self.fundo_Codigo_produto.place(relx= 0.05, rely = 0.1, relheight=0.11, relwidth=0.21)
    #entry
    self.et_Codigo_produto = Entry(self.FR_root_ator_5, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Codigo_produto.place(relx= 0.065, rely = 0.115, relheight= 0.075, relwidth=0.185)
    self.et_Codigo_produto.focus()
    
    #codigo do Produto
    #label
    self.label_Codigo_pet = Label(self.FR_root_ator_5, text="Código do Pet", font=(fonte, 10), background=fundo3)
    self.label_Codigo_pet.place(relx= 0.3, rely = 0.05)
    #imagem de fundo
    self.fundo_Codigo_pet = Label(self.FR_root_ator_5, image= self.img_fundo)
    self.fundo_Codigo_pet.place(relx= 0.3, rely = 0.1, relheight=0.11, relwidth=0.21)
    #entry
    self.et_Codigo_pet = Entry(self.FR_root_ator_5, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Codigo_pet.place(relx= 0.315, rely = 0.115, relheight= 0.075, relwidth=0.185)
    
    #codigo de encomenda
    #label
    self.label_Codigo_pet = Label(self.FR_root_ator_5, text="Código da Encomenda", font=(fonte, 10), background=fundo3)
    self.label_Codigo_pet.place(relx= 0.55, rely = 0.05)
    #imagem de fundoS
    self.fundo_Codigo_pet = Label(self.FR_root_ator_5, image= self.img_fundo)
    self.fundo_Codigo_pet.place(relx= 0.55, rely = 0.1, relheight=0.11, relwidth=0.21)
    #entry
    self.et_Codigo_pet = Entry(self.FR_root_ator_5, bd = 0, bg = "#ffffff", highlightthickness = 0, font= fonte)
    self.et_Codigo_pet.place(relx= 0.565, rely = 0.115, relheight= 0.075, relwidth=0.185)

    self.lista1 = ttk.Treeview(self.FR_lista_compra, height=3, columns=("col1", "col2", "col3"))
    self.lista1.heading("#0", text="")
    self.lista1.heading("#1", text="Codigo")
    self.lista1.heading("#2", text="Nome")
    self.lista1.heading("#3", text="Valor")
    
    self.lista1.column("#0",width=1)
    self.lista1.column("#1",width=60)
    self.lista1.column("#2",width=150)
    self.lista1.column("#3",width=100)
    
    self.lista1.place(relx = 0.0, rely = 0.0, relheight= 0.8, relwidth=1.0)
    
    self.lista2 = ttk.Treeview(self.FR_lista_compra, height=3, columns=("col1", "col2", "col3"))
    self.lista2.heading("#0", text="")
    self.lista2.heading("#1", text="")
    self.lista2.heading("#2", text="")
    self.lista2.heading("#3", text="Total")
    
    self.lista2.column("#0",width=1)
    self.lista2.column("#1",width=60)
    self.lista2.column("#2",width=150)
    self.lista2.column("#3",width=100)
    
    self.lista2.place(relx = 0.0, rely = 0.8, relheight= 0.2, relwidth=1.0)
    
    #Botões
    #Finalizar
    self.bt_finalizar = Button(self.FR_root_ator_5, image= self.img_bt_finalizar, borderwidth = 0, highlightthickness = 0, command= lambda: muda_frame_funcionalidade(self, "Nota"))
    self.bt_finalizar.place(relx= 0.68, rely = 0.87, relheight= 0.11, relwidth=0.29)
    
    #Cancelar
    self.bt_cancelar = Button(self.FR_root_ator_5, image= self.img_bt_cancelar, borderwidth = 0, highlightthickness = 0)
    self.bt_cancelar.place(relx= 0.34, rely = 0.86, relheight= 0.13, relwidth=0.32)
    
    #Limpar
    self.bt_limpar = Button(self.FR_root_ator_5, image= self.img_bt_limpar, borderwidth = 0, highlightthickness = 0)
    self.bt_limpar.place(relx= 0.02, rely = 0.86, relheight= 0.13, relwidth=0.32)
    
    #Adicionar
    # Modded by Erineldo 26/05
    # Corrigindo erros de nomenclatura bt_limpar->bt_adicionar
    self.bt_adicionar = Button(self.FR_root_ator_5, image= self.img_bt_adicionar, borderwidth = 0, highlightthickness = 0)
    self.bt_adicionar.place(relx= 0.79, rely = 0.09, relheight= 0.115, relwidth=0.175)

def Nota_fiscal(self):
    self.FR_root_ator_6 = Frame(self.root, background = fundo3, highlightbackground = "#000000", borderwidth=0.01, highlightthickness=2)
    self.FR_root_ator_6.place(relx = 0.337, rely = 0.0, relheight = 1.0, relwidth= 0.663)
    self.FR_lista_nota = Frame(self.FR_root_ator_6, background = "#ffffff", highlightbackground = "#000000", borderwidth=0.01, highlightthickness=2)
    self.FR_lista_nota.place(relx = 0.01, rely = 0.05, relheight = 0.8, relwidth= 0.98)
    
    self.LB_label1 = Label(self.FR_root_ator_6, text = "Nota Fiscal", background = fundo3)
    self.LB_label1.pack()
    
    self.frame_funcionalidade = self.FR_root_ator_6
    
    self.img_ok = PhotoImage(file= Path(ROOT_DIR, "img", "botao_OK.png"))
    
    self.lista1 = ttk.Treeview(self.FR_lista_nota, height=3, columns=("col1", "col2", "col3"))
    self.lista1.heading("#0", text="")
    self.lista1.heading("#1", text="Codigo")
    self.lista1.heading("#2", text="Nome")
    self.lista1.heading("#3", text="Valor")
    
    self.lista1.column("#0",width=1)
    self.lista1.column("#1",width=60)
    self.lista1.column("#2",width=150)
    self.lista1.column("#3",width=100)
    
    self.lista1.place(relx = 0.0, rely = 0.0, relheight= 0.85, relwidth=1.0)
    
    self.lista2 = ttk.Treeview(self.FR_lista_nota, height=3, columns=("col1", "col2", "col3"))
    self.lista2.heading("#0", text="")
    self.lista2.heading("#1", text="")
    self.lista2.heading("#2", text="")
    self.lista2.heading("#3", text="Total")
    
    self.lista2.column("#0",width=1)
    self.lista2.column("#1",width=60)
    self.lista2.column("#2",width=150)
    self.lista2.column("#3",width=100)
    
    self.lista2.place(relx = 0.00, rely = 0.85, relheight= 0.15, relwidth=1.0)
    
    #Botões
    #Salvar
    self.bt_salvar = Button(self.FR_root_ator_6, image= self.img_ok, borderwidth = 0, highlightthickness = 0,command= lambda: muda_frame_funcionalidade(self, "Produtos"))
    self.bt_salvar.place(relx= 0.8, rely = 0.86, relheight= 0.115, relwidth=0.175)

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
    elif(frame == "Encomenda"):
        self.frame_funcionalidade.destroy()
        Encomenda_Pet(self)  
    elif(frame == "Nota"):
        self.frame_funcionalidade.destroy()
        Nota_fiscal(self)
        
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

# Mod by Erineldo 26/05
# Correção de erros de nomenclatura
def muda_lista_venda_pet(self, opcao):
    if(opcao == "COD-PET"):
        self.atual_lista.destroy()
        lista_pets_venda(self)
    elif(opcao == "COD-DONO"):
        self.atual_lista.destroy()
        lista_donos(self)
    elif(opcao == "NA"):
        self.atual_lista.destroy()

def duploClick_CODPet(self):
        limpa_campos_vendaPet_CODPet(self)
        for i in self.lista1.selection():
            col1, col2, col3, col4, col5 = self.lista1.item(i, 'values')
            self.et_Codigo_pet.insert(END, col1)
def duploClick_CODDono(self):
        limpa_campos_vendaPet_CODDono(self)
        for i in self.lista1.selection():
            col1, col2, col3 = self.lista1.item(i, 'values')
            self.et_Codigo_dono.insert(END, col1)

def item_Selecionado(self):
    for item in self.lista1.selection():
        item_text = self.lista1.item(item, "values")
        print(item_text)

def lista_pets_venda(self):
        self.FR_lista1 = Frame(self.FR_root_ator_4, background = "#ffffff", highlightbackground = "#000000", borderwidth=0.01, highlightthickness=2)
        self.FR_lista1.place(relx = 0.33, rely = 0.1, relheight = 0.75, relwidth= 0.65)
        
        self.atual_lista = self.FR_lista1
        
        self.lista1 = ttk.Treeview(self.FR_lista1, height=3, columns=("col1", "col2", "col3", "col4", "col5"))
        self.lista1.heading("#0", text="")
        self.lista1.heading("#1", text="Codigo")
        self.lista1.heading("#2", text="Idade")
        self.lista1.heading("#3", text="Sexo")
        self.lista1.heading("#4", text="Raça")
        self.lista1.heading("#5", text="Valor")
        
        # Modded by Erineldo 27/05
        # Modificado tamanho das colunas
        self.lista1.column("#0",width=0)
        self.lista1.column("#1",width=25)
        self.lista1.column("#2",width=30)
        self.lista1.column("#3",width=20)
        self.lista1.column("#4",width=40)
        self.lista1.column("#5",width=30)

        # Inserir os dados na tabela
        # tree.insert('', tkinter.END, values=data)
        # Modded by Erineldo 26/05
        # Adicionada a listagem de pets disponíveis para venda
        dados = gerenciador_BD.BD.get_pets_venda(self)
        for pet_venda in dados:
            self.lista1.insert('', tkinter.END, values=pet_venda)
        
        self.label_Codigo_venda_pet = Label(self.FR_lista1, text="Pets disponíveis para venda", font=fonte, background="#ffffff")
        self.label_Codigo_venda_pet.place(relx= 0.2, rely = 0.0)
        
        self.lista1.place(relx = 0.0, rely = 0.1, relheight= 0.9, relwidth=1.0)
        
        self.lista1.bind('<Double-1>', lambda x: duploClick_CODPet(self))
        
def lista_donos(self):
        self.FR_lista2 = Frame(self.FR_root_ator_4, background = "#ffffff", highlightbackground = "#000000", borderwidth=0.01, highlightthickness=2)
        self.FR_lista2.place(relx = 0.33, rely = 0.1, relheight = 0.75, relwidth= 0.65)
        
        self.atual_lista = self.FR_lista2
        
        self.lista1 = ttk.Treeview(self.FR_lista2, height=3, columns=("col1", "col2", "col3"))
        self.lista1.heading("#0", text="")
        self.lista1.heading("#1", text="Codigo")
        self.lista1.heading("#2", text="Nome")
        self.lista1.heading("#3", text="Contato")
        
        # Modded by Erineldo 27/05
        # Modificado o tamanho das colunas
        self.lista1.column("#0",width=1)
        self.lista1.column("#1",width=60)
        self.lista1.column("#2",width=120)
        self.lista1.column("#3",width=130)
        
        # Added by Erineldo 27/05
        # Listagem de clientes
        dados = gerenciador_BD.BD.get_clientes(self)
        for cliente in dados:
            self.lista1.insert('', tkinter.END, values=cliente)

        self.lista1.bind('<<TreeviewSelect>>', item_Selecionado(self))

        
        self.label_Codigo_venda_pet = Label(self.FR_lista2, text="Lista Clientes Cadastrados", font=fonte, background="#ffffff")
        self.label_Codigo_venda_pet.place(relx= 0.2, rely = 0.0)
        
        self.lista1.place(relx = 0.0, rely = 0.1, relheight= 0.9, relwidth=1.0) 
        
        self.lista1.bind('<Double-1>', lambda x: duploClick_CODDono(self))