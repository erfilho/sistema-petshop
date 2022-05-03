from tkinter import *

fundo1 = '#4B0082'
fundo2 = '#7B68EE'
fundo3 = '#8A2BE2'
borda = '#BA55D3'

#atual_frame = Frame()
    
def Estoquista(self):
    self.FR_root_1 = Frame(self.root, background = fundo2, highlightbackground = borda, borderwidth=0.01, highlightthickness=2)
    self.FR_root_1.place(relx = 0.01, rely = 0.01, relheight = 0.98, relwidth= 0.3)
    
    self.root.title("Estoquista")
    
    self.FR_dados_ator = Frame(self.FR_root_1, background = fundo3, highlightbackground = borda, borderwidth = 0.01, highlightthickness=2)
    self.FR_dados_ator.place(relx = 0.01, rely = 0.01, relheight = 0.2, relwidth= 0.98)
    
    self.LB_saudacao = Label(self.FR_dados_ator, text = "Bom dia", background = fundo3)
    self.LB_saudacao.place(relx = 0.02, rely = 0.02)
    
    self.LB_cpf = Label(self.FR_dados_ator, text = "CPF", background = fundo3)
    self.LB_cpf.place(relx = 0.02, rely = 0.4)
    
    self.LB_cargo = Label(self.FR_dados_ator, text = "CARGO", background = fundo3)
    self.LB_cargo.place(relx = 0.02, rely = 0.73)

    self.LB_label1 = Label(self.FR_root_1, text = "Selecione a opção de Cadastro", background = fundo2)
    self.LB_label1.place(relx = 0.02, rely = 0.22)
    
    lista = ["Produtos", "Pets"]
    value_inside = StringVar()
    value_inside.set(lista[0])
    self.OP_Cadastro = OptionMenu(self.FR_root_1, value_inside, *lista)
    self.OP_Cadastro.place(relx = 0.03, rely = 0.28)
    
    self.bt_OK = Button(self.FR_root_1 , text="Logout")
    self.bt_OK.place(relx= 0.69, rely = 0.93)

def Recepcionista(self):
    self.FR_root_2 = Frame(self.root, background = fundo2, highlightbackground = borda, borderwidth=0.01, highlightthickness=2)
    self.FR_root_2.place(relx = 0.01, rely = 0.01, relheight = 0.98, relwidth= 0.3)

    self.root.title("Recepcionista")
    atual_frame = self.FR_root_2
    
    self.FR_dados_ator = Frame(self.FR_root_2, background = fundo3, highlightbackground = borda, borderwidth = 0.01, highlightthickness=2)
    self.FR_dados_ator.place(relx = 0.01, rely = 0.01, relheight = 0.2, relwidth= 0.98)
    
    self.LB_saudacao = Label(self.FR_dados_ator, text = "Bom dia", background = fundo3)
    self.LB_saudacao.place(relx = 0.02, rely = 0.02)
    
    self.LB_cpf = Label(self.FR_dados_ator, text = "CPF", background = fundo3)
    self.LB_cpf.place(relx = 0.02, rely = 0.4)
    
    self.LB_cargo = Label(self.FR_dados_ator, text = "CARGO", background = fundo3)
    self.LB_cargo.place(relx = 0.02, rely = 0.73)

    self.LB_label1 = Label(self.FR_root_2, text = "Cadastro", background = fundo2)
    self.LB_label1.place(relx = 0.02, rely = 0.22)
    
    lista1 = ["Clientes"]
    value_inside = StringVar()
    value_inside.set(lista1[0])
    self.OP_Cadastro = OptionMenu(self.FR_root_2, value_inside, *lista1)
    self.OP_Cadastro.place(relx = 0.03, rely = 0.28)
    
    self.LB_label1 = Label(self.FR_root_2, text = "Vendas", background = fundo2)
    self.LB_label1.place(relx = 0.02, rely = 0.35)
    
    lista2 = ["Pets"]
    value_inside = StringVar()
    value_inside.set(lista2[0])
    self.OP_Vendas = OptionMenu(self.FR_root_2, value_inside, *lista2)
    self.OP_Vendas.place(relx = 0.03, rely = 0.4)
    
    self.bt_OK = Button(self.FR_root_2, text="Logout")
    self.bt_OK.place(relx= 0.69, rely = 0.93)
    
def Caixa(self):
    self.FR_root_3 = Frame(self.root, background = fundo2, highlightbackground = borda, borderwidth=0.01, highlightthickness=2)
    self.FR_root_3.place(relx = 0.01, rely = 0.01, relheight = 0.98, relwidth= 0.3)

    self.root.title("Caixa")
    self.atual_frame = self.FR_root_3

    self.FR_dados_ator = Frame(self.FR_root_3, background = fundo3, highlightbackground = borda, borderwidth = 0.01, highlightthickness=2)
    self.FR_dados_ator.place(relx = 0.01, rely = 0.01, relheight = 0.2, relwidth= 0.98)

    self.LB_saudacao = Label(self.FR_dados_ator, text = "Bom dia", background = fundo3)
    self.LB_saudacao.place(relx = 0.02, rely = 0.02)

    self.LB_cpf = Label(self.FR_dados_ator, text = "CPF", background = fundo3)
    self.LB_cpf.place(relx = 0.02, rely = 0.4)

    self.LB_cargo = Label(self.FR_dados_ator, text = "CARGO", background = fundo3)
    self.LB_cargo.place(relx = 0.02, rely = 0.73)

    self.LB_label1 = Label(self.FR_root_3, text = "Vendas", background = fundo2)
    self.LB_label1.place(relx = 0.02, rely = 0.22)


    lista = ["Produtos"]
    value_inside = StringVar()
    value_inside.set(lista[0])
    self.OP_Vendas = OptionMenu(self.FR_root_3, value_inside, *lista)
    self.OP_Vendas.place(relx = 0.03, rely = 0.28)

    self.bt_OK = Button(self.FR_root_3, text="Logout")
    self.bt_OK.place(relx= 0.69, rely = 0.93)