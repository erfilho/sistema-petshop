from tkinter import *
from tkinter import messagebox
import gerenciador_BD

fundo1 = '#4B0082'
fundo2 = '#7B68EE'
fundo3 = '#8A2BE2'
borda = '#BA55D3'

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
        
        self.et_Senha = Entry(self.frame_1, show='*')
        self.et_Senha.place(relx= 0.4, rely = 0.35)

        #Criando os Botões
        self.bt_OK = Button(self.frame_1, text="OK", command = lambda: muda_tela_ator(self, gerenciador_BD.BD.verifica_senha(self, self.et_cpf.get(), self.et_Senha.get())))
        self.bt_OK.place(relx= 0.47, rely = 0.42)

def Estoquista(self, lista):
    self.FR_root_1 = Frame(self.root, background = fundo2, highlightbackground = borda, borderwidth=0.01, highlightthickness=2)
    self.FR_root_1.place(relx = 0.01, rely = 0.01, relheight = 0.98, relwidth= 0.3)
    
    self.root.title("Estoquista")
    atual_frame = self.FR_root_1
    
    Cadastro_Produto(self)
    
    self.FR_dados_ator = Frame(self.FR_root_1, background = fundo3, highlightbackground = borda, borderwidth = 0.01, highlightthickness=2)
    self.FR_dados_ator.place(relx = 0.01, rely = 0.01, relheight = 0.2, relwidth= 0.98)
    
    self.LB_saudacao = Label(self.FR_dados_ator, text = "Bom dia", background = fundo3)
    self.LB_saudacao.place(relx = 0.02, rely = 0.02)
    self.LB_nome = Label(self.FR_dados_ator, text = lista[1], background = fundo3)
    self.LB_nome.place(relx = 0.4, rely = 0.02)
    
    self.LB_cpf = Label(self.FR_dados_ator, text = "CPF", background = fundo3)
    self.LB_cpf.place(relx = 0.02, rely = 0.4)
    self.LB_cpf_f = Label(self.FR_dados_ator, text = lista[2], background = fundo3)
    self.LB_cpf_f.place(relx = 0.4, rely = 0.4)
    
    self.LB_cargo = Label(self.FR_dados_ator, text = "CARGO", background = fundo3)
    self.LB_cargo.place(relx = 0.02, rely = 0.73)
    self.LB_cargo_f = Label(self.FR_dados_ator, text = lista[0], background = fundo3)
    self.LB_cargo_f.place(relx = 0.4, rely = 0.73)
    
    self.LB_label1 = Label(self.FR_root_1, text = "Selecione a opção de Cadastro", background = fundo2)
    self.LB_label1.place(relx = 0.02, rely = 0.22)
    
    self.lista_estoquista = ["Produto", "Pet"]
    self.value_inside = StringVar()
    self.value_inside.set(self.lista_estoquista[0])
    
    self.OP_Cadastro = OptionMenu(self.FR_root_1, self.value_inside, *self.lista_estoquista, command = lambda x: muda_frame_funcionalidade(self, self.value_inside.get()))
    self.OP_Cadastro.place(relx = 0.03, rely = 0.28)
    
    self.bt_OK = Button(self.FR_root_1 , text="Logout", command = lambda: Logout(self))
    self.bt_OK.place(relx= 0.69, rely = 0.93)

def Recepcionista(self, lista):
    self.FR_root_2 = Frame(self.root, background = fundo2, highlightbackground = borda, borderwidth=0.01, highlightthickness=2)
    self.FR_root_2.place(relx = 0.01, rely = 0.01, relheight = 0.98, relwidth= 0.3)

    self.root.title("Recepcionista")
    atual_frame = self.FR_root_2
    
    Cadastro_Cliente(self)
    
    self.FR_dados_ator = Frame(self.FR_root_2, background = fundo3, highlightbackground = borda, borderwidth = 0.01, highlightthickness=2)
    self.FR_dados_ator.place(relx = 0.01, rely = 0.01, relheight = 0.2, relwidth= 0.98)
    
    self.LB_saudacao = Label(self.FR_dados_ator, text = "Bom dia", background = fundo3)
    self.LB_saudacao.place(relx = 0.02, rely = 0.02)
    self.LB_nome = Label(self.FR_dados_ator, text = lista[1], background = fundo3)
    self.LB_nome.place(relx = 0.4, rely = 0.02)
    
    self.LB_cpf = Label(self.FR_dados_ator, text = "CPF", background = fundo3)
    self.LB_cpf.place(relx = 0.02, rely = 0.4)
    self.LB_cpf_f = Label(self.FR_dados_ator, text = lista[2], background = fundo3)
    self.LB_cpf_f.place(relx = 0.4, rely = 0.4)
    
    self.LB_cargo = Label(self.FR_dados_ator, text = "CARGO", background = fundo3)
    self.LB_cargo.place(relx = 0.02, rely = 0.73)
    self.LB_cargo_f = Label(self.FR_dados_ator, text = lista[0], background = fundo3)
    self.LB_cargo_f.place(relx = 0.4, rely = 0.73)
    
    self.LB_label1 = Label(self.FR_root_2, text = "Cadastro", background = fundo2)
    self.LB_label1.place(relx = 0.02, rely = 0.22)
    
    lista_recepcionista1 = ["Clientes"]
    self.value_inside1 = StringVar()
    self.value_inside1.set(lista_recepcionista1[0])
    
    self.OP_Cadastro = OptionMenu(self.FR_root_2, self.value_inside1, *lista_recepcionista1, command = lambda x:  muda_frame_funcionalidade(self, self.value_inside1.get()))
    self.OP_Cadastro.place(relx = 0.03, rely = 0.28)
    
    self.LB_label1 = Label(self.FR_root_2, text = "Vendas", background = fundo2)
    self.LB_label1.place(relx = 0.02, rely = 0.35)
    
    lista_recepcionista2 = ["Pets"]
    self.value_inside2 = StringVar()
    self.value_inside2.set(lista_recepcionista2[0])
    
    self.OP_Vendas = OptionMenu(self.FR_root_2, self.value_inside2, *lista_recepcionista2, command = lambda x:  muda_frame_funcionalidade(self, self.value_inside2.get()))
    self.OP_Vendas.place(relx = 0.03, rely = 0.4)
    
    self.bt_OK = Button(self.FR_root_2, text="Logout", command = lambda: Logout(self))
    self.bt_OK.place(relx= 0.69, rely = 0.93)
    
def Caixa(self, lista):
    
    self.FR_root_3 = Frame(self.root, background = fundo2, highlightbackground = borda, borderwidth=0.01, highlightthickness=2)
    self.FR_root_3.place(relx = 0.01, rely = 0.01, relheight = 0.98, relwidth= 0.3)
    
    self.root.title("Caixa")
    self.atual_frame = self.FR_root_3

    Vendas(self)
    
    self.FR_dados_ator = Frame(self.FR_root_3, background = fundo3, highlightbackground = borda, borderwidth = 0.01, highlightthickness=2)
    self.FR_dados_ator.place(relx = 0.01, rely = 0.01, relheight = 0.2, relwidth= 0.98)

    self.LB_saudacao = Label(self.FR_dados_ator, text = "Bom dia", background = fundo3)
    self.LB_saudacao.place(relx = 0.02, rely = 0.02)
    self.LB_nome = Label(self.FR_dados_ator, text = lista[1], background = fundo3)
    self.LB_nome.place(relx = 0.4, rely = 0.02)
    
    self.LB_cpf = Label(self.FR_dados_ator, text = "CPF", background = fundo3)
    self.LB_cpf.place(relx = 0.02, rely = 0.4)
    self.LB_cpf_f = Label(self.FR_dados_ator, text = lista[2], background = fundo3)
    self.LB_cpf_f.place(relx = 0.4, rely = 0.4)
    
    self.LB_cargo = Label(self.FR_dados_ator, text = "CARGO", background = fundo3)
    self.LB_cargo.place(relx = 0.02, rely = 0.73)
    self.LB_cargo_f = Label(self.FR_dados_ator, text = lista[0], background = fundo3)
    self.LB_cargo_f.place(relx = 0.4, rely = 0.73)
    
    self.LB_label1 = Label(self.FR_root_3, text = "Vendas", background = fundo2)
    self.LB_label1.place(relx = 0.02, rely = 0.22)

    lista_caixa = ["Produtos"]
    self.value_inside = StringVar()
    self.value_inside.set(lista[0])
    self.OP_Vendas = OptionMenu(self.FR_root_3, self.value_inside, *lista_caixa, command = lambda x:  muda_frame_funcionalidade(self, self.value_inside.get()))
    self.OP_Vendas.place(relx = 0.03, rely = 0.28)

    self.bt_OK = Button(self.FR_root_3, text="Logout", command = lambda: Logout(self))
    self.bt_OK.place(relx= 0.69, rely = 0.93)

def Cadastro_Produto(self):
    self.FR_root_ator_1 = Frame(self.root, background = fundo2, highlightbackground = borda, borderwidth=0.01, highlightthickness=2)
    self.FR_root_ator_1.place(relx = 0.32, rely = 0.01, relheight = 0.98, relwidth= 0.67)
    
    self.frame_funcionalidade = self.FR_root_ator_1

    self.LB_label1 = Label(self.FR_root_ator_1, text = "Cadastro Produtos", background = fundo2)
    self.LB_label1.pack()

def Cadastro_Pet(self):
    self.FR_root_ator_2 = Frame(self.root, background = fundo2, highlightbackground = borda, borderwidth=0.01, highlightthickness=2)
    self.FR_root_ator_2.place(relx = 0.32, rely = 0.01, relheight = 0.98, relwidth= 0.67)
    
    self.frame_funcionalidade = self.FR_root_ator_2

    self.LB_label1 = Label(self.FR_root_ator_2, text = "Cadastro Pet", background = fundo2)
    self.LB_label1.pack()
    
def Cadastro_Cliente(self):
    self.FR_root_ator_3 = Frame(self.root, background = fundo2, highlightbackground = borda, borderwidth=0.01, highlightthickness=2)
    self.FR_root_ator_3.place(relx = 0.32, rely = 0.01, relheight = 0.98, relwidth= 0.67)
    
    self.frame_funcionalidade = self.FR_root_ator_3

    self.LB_label1 = Label(self.FR_root_ator_3, text = "Cadastro Clientes", background = fundo2)
    self.LB_label1.pack()

def Vendas(self):
    self.FR_root_ator_4 = Frame(self.root, background = fundo2, highlightbackground = borda, borderwidth=0.01, highlightthickness=2)
    self.FR_root_ator_4.place(relx = 0.32, rely = 0.01, relheight = 0.98, relwidth= 0.67)
    
    self.frame_funcionalidade = self.FR_root_ator_4

    self.LB_label1 = Label(self.FR_root_ator_4, text = "Vendas", background = fundo2)
    self.LB_label1.pack()

def Venda_Pet(self):
    self.FR_root_ator_4 = Frame(self.root, background = fundo2, highlightbackground = borda, borderwidth=0.01, highlightthickness=2)
    self.FR_root_ator_4.place(relx = 0.32, rely = 0.01, relheight = 0.98, relwidth= 0.67)
    
    self.frame_funcionalidade = self.FR_root_ator_4

    self.LB_label1 = Label(self.FR_root_ator_4, text = "Venda Pet", background = fundo2)
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
        