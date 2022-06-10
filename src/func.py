# Importa o módulo de popup de mensagens do tkinter
from contextlib import nullcontext
from email import message_from_string
from tkinter import messagebox
import tkinter

from numpy import double
# Importa o módulo de exibição das telas
import frames as frames
# Importação do arquivo de controle do banco de dados
import control_db as cdb
# Importa o módulo para verificação de dados com expressões regulares
import re

# Função que vai mudar as funcionalidades do sistema de acordo com o tipo de usuário
def muda_tela(self, lista):
    try:
        if type(lista) is list:
            if len(lista) > 0:
                for i in lista:
                    cargo = i[0]
                if cargo == 'ESTOQUISTA':
                    self.frame_atual.destroy
                    frames.Estoquista(self, i)
                elif cargo == 'RECEPCIONISTA':
                    self.frame_atual.destroy
                    frames.Recepcionista(self, i)
                elif cargo == 'CAIXA':
                    self.frame_atual.destroy
                    frames.Caixa(self, i)
            else:
                raise Exception('Cargo não encontrado, tente novamente!')
        else:
            raise Exception('Funcionário não encontrado!')
    except Exception as erro:
        self.msgErro = messagebox.showerror('Erro', erro)

# Função que vai mudar a tela de cadastro de pets
def muda_venda_pet(self, opcao):
    if(opcao == "COD-PET"):
        self.atual_lista.destroy()
        frames.lista_pets_venda(self)
    elif(opcao == "COD-DONO"):
        self.atual_lista.destroy()
        frames.lista_donos(self)
    elif(opcao == "NA"):
        self.atual_lista.destroy()

# Função que vai mudar as telas do sistema, cadastros, vendas e afins
def muda_funcionalidade(self, frame):
    try:
        if frame == "Produto":
            self.frame_funcionalidade.destroy()
            frames.Cadastro_Produto(self)
        elif(frame == "Pet"):
            self.frame_funcionalidade.destroy()
            frames.Cadastro_Pet(self)
        elif(frame == "Clientes"):
            self.frame_funcionalidade.destroy()
            frames.Cadastro_Cliente(self)
        elif(frame == "Pets"):
            self.frame_funcionalidade.destroy()
            frames.Venda_Pet(self)  
        elif(frame == "Produtos"):
            self.frame_funcionalidade.destroy()
            frames.Vendas(self)
        elif(frame == "Encomenda"):
            self.frame_funcionalidade.destroy()
            frames.Encomenda_Pet(self)  
        elif(frame == "Nota"):
            self.frame_funcionalidade.destroy()
            frames.Nota_fiscal(self)
        else:
            raise Exception('Funcionalidade não encontrada, erro interno!')
    except Exception as erro:
        self.msgErro = messagebox.showerror('Erro', erro)

# Função que vai executar a ação de logout do sistema
def logout(self):
    self.frame_funcionalidade.destroy()
    self.frame_atual.destroy()
    frames.Login(self)

# Função que vai limpar os campos da tela de cadastro de produtos
def clean_produtos(self):
    self.msgBox = messagebox.askyesno('Limpar os campos', 'Deseja realmente limpar os campos ?')
    if(self.msgBox):
        self.et_Codigo.delete(0, 'end')
        self.et_Nome.delete(0, 'end')
        self.et_Preco.delete(0, 'end')

# Função que vai limpar os campos da tela de cadastro de pets
def clean_pets(self):
    self.msgBox = messagebox.askyesno('Limpar os campos', 'Deseja realmente limpar os campos ?')
    if(self.msgBox):
        self.et_Codigo.delete(0, 'end')
        self.et_Nome.delete(0, 'end')
        self.et_Idade.delete(0, 'end')
        self.et_Sexo.delete(0, 'end')
        self.et_Codigo_Dono.delete(0, 'end')
        self.et_Raca.delete(0, 'end')
        self.et_Preco.delete(0, 'end')
        self.CB_pet_para_venda.deselect()

# Função que vai limpar os campos da tela de cadastro de clientes
def clean_clientes(self):
    self.msgBox = messagebox.askyesno('Limpar os campos', 'Deseja realmente limpar os campos ?')
    if(self.msgBox):
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

# Função que vai limpar os campos da tela de cadastro de encomendas
def clean_encomendas(self):
    self.msgBox = messagebox.askyesno('Limpar os campos', 'Deseja realmente limpar os campos ?')
    if(self.msgBox):
        self.et_Codigo_encomenda.delete(0, 'end')
        self.et_Codigo_cli.delete(0, 'end')
        self.et_Raca.delete(0, 'end')
        self.et_Sexo.delete(0, 'end')
        self.et_Idade.delete(0, 'end')
        self.et_Valor.delete(0, 'end')
        self.et_Codigo_pet.delete(0, 'end')

# Função que vai limpar os campos da tela de vendas
def clean_vendas(self, opcao = 0):
    if(opcao == 0):
        self.msgBox = messagebox.askyesno('Limpar os campos', 'Deseja realmente limpar os campos ?')
        if(self.msgBox):
            self.et_Codigo_produto.delete(0, 'end')
            self.et_Codigo_pet.delete(0, 'end')
            self.et_Codigo_encomenda.delete(0, 'end')
    elif(opcao == 1):
        self.et_Codigo_produto.delete(0, 'end')
        self.et_Codigo_pet.delete(0, 'end')
        self.et_Codigo_encomenda.delete(0, 'end')

# Função que vai limpar os campos da tela de vendas de pet
def clean_venda_pet(self, opcao = 0):
    if(opcao == 0):
        self.msgBox = messagebox.askyesno('Limpar os campos', 'Deseja realmente limpar os campos ?')
        if(self.msgBox):
            self.et_Codigo_pet.delete(0, 'end')
            self.et_Codigo_dono.delete(0, 'end')
            self.et_Codigo_venda_pet.delete(0, 'end')
    elif(opcao == 1):
        self.et_Codigo_pet.delete(0, 'end')
    elif(opcao == 2):
        self.et_Codigo_dono.delete(0, 'end')

#Função que limpa a tabela de vendas
def clean_tabela_venda(self, opcao = 0):
    if(opcao == 0):
        self.msgBox = messagebox.askyesno('Cancelamento de venda', 'Deseja realmente cancelar a venda ?')
        if(self.msgBox):
            self.lista_venda_1.delete(*self.lista_venda_1.get_children())
            self.lista_venda_2.delete(*self.lista_venda_2.get_children())
    if(opcao == 1):
        self.lista_venda_2.delete(*self.lista_venda_2.get_children())
# Função que vai validar o cpf
def valida_cpf(cpf):
    # Aqui ocorre o tratamento de excessões
    try:
        # Verifica se o valor passado é realmente um cpf
        if len(cpf) == 14:
            # Cria um padrão de verificação do cpf
            pattern = re.compile(r"^(\d{3}.){2}\d{3}-\d{2}$")
            # Verifica se o cpf se encontra no padrão
            if re.match(pattern, cpf):
                # Caso esteja no padrão será retornado TRUE
                return 1
            # Caso não seja será retornado FALSE
            else:
                return 0
        # Caso não seja será retornado FALSE
        else:
            return 0
    except Exception as erro:
        # Se ocorrer alguma exceção também será retornado FALSE
        return 0

# Função que vai validar o número de telefone
def valida_cel(cel):
    # Aqui ocorre o tratamento de exceções
    try:
        # Verifica se o valor passado é realmente um número de celular
        if len(cel) == 14:
            # Cria um padrão de verificação para o número do celular
            pattern = re.compile(r"^\(\d{2}\)\d{5}\-\d{4}$")
            # Verifica se o número do celular se encontra no padrão
            if re.match(pattern, cel):
                # Caso esteja no padrão, será retornado TRUE
                return 1
            # Caso não esteja, será retornado FALSE
            else:
                return 0
        # Caso não esteja, será retornado FALSE
        else:
            return 0
    # Caso ocorra alguma exceção será tratada aqui
    except Exception as erro:
        # Caso ocorra alguma, será retornado FALSE
        return 0

# Função que vai validar o email
def valida_email(email):
    # Aqui ocorre o tratamento de exceções
    try:
        # Verifica se realmente foi passado um email
        if len(email) > 0:
            # Cria um padrão de verificação para o email
            pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
            # Verifica se o email se encontra no padrão
            if re.match(pattern, email):
                # Caso seja, será retornado verdadeiro
                return 1
            else:
            # Caso não seja será retornado falso
                return 0
        else:
            # Caso não seja será retornado falso
            return 0
    # Caso ocorra alguma exceção será tratada aqui
    except Exception as erro:
        # Se ocorrer alguma será retornado falso
        return 0

# Função que vai validar o código
def valida_cod(cod):
    # Aqui ocorre o tratamento de exceções
    try:
        # Verifica se realmente foi passado um código e está entre 4 dígitos
        if len(cod) > 0 and len(cod) < 5:
            # Cria o padrão para ser verificado o código
            pattern = re.compile(r'^(\d{0,4})$')
            # Verifica se o código se encontra no padrão
            if re.match(pattern, cod):
                # Caso se encontre retorna verdadeiro
                return 1
            else:
                # Caso não seja será retornado falso
                return 0
        else:
            # Caso não tenha sido, será retornado falso
            return 0
    # Caso ocorra alguma exceção seja tratada aqui
    except Exception as erro:
        # Se ocorrer alguma será retornado falso
        return 0

#Função que adiciona com dois clickes o código do pet no campo Código do Pet
def duploClick_CODPet(self):
    clean_venda_pet(self, 1)
    for i in self.lista_pet_venda.selection():
        col1, col2, col3, col4, col5 = self.lista_pet_venda.item(i, 'values')
        self.et_Codigo_pet.insert('end', col1)
        
#Função que adiciona com dois clickes o código do dono no campo Código do Dono
def duploClick_CODDono(self):
    clean_venda_pet(self, 2)
    for i in self.lista_dono.selection():
        col1, col2, col3 = self.lista_dono.item(i, 'values')
        self.et_Codigo_dono.insert('end', col1)
      
#Função que insere produtos na tabela de venda
def adiciona_venda_produto(self, prod, pet, enc):
    # Aqui ocorre o tratamento de excessões
    try:
        clean_vendas(self, 1)   #Limpa os campos de códigos após clicar em Adicionar.
        if(prod != ''): #Verifica se o código do pet é diferente de vazio.
            lista = cdb.Lists.produto_comum(self, 'CODIGO', prod)   #Recebe a lista com os dados do pet referentes ao código recebido.
            if type(lista) is list: #Verifica se o retorno é o tipo lista.
                if len(lista) > 0:  #verifica se a lista se a lista retornada está vazia.
                    lista = list(lista[0])  #tranforma a tupla no interior da lista em um lista .
                    lista.insert(1,'Produto') #insere o tipo do produto na lista.
                    lista = [lista] #Tranforma a lista novamente em tupla.
                    for i in lista:
                        self.lista_venda_1.insert('', tkinter.END, values=i)    #Insere a lista nos campos da tabela.
                else:
                    self.msgBox = messagebox.showinfo('Produto não encotrado', 'O Produto não foi encontrado.') #retorena uma mensagem caso o código digitado não coresponda a algum produto.
        elif(pet != ''):
            lista = cdb.Lists.produto_pet(self, 'CODIGO', pet)
            if type(lista) is list:
                if len(lista) > 0:
                    lista = list(lista[0])
                    lista.insert(1,'Pet')
                    lista = [lista]
                    for i in lista:
                        self.lista_venda_1.insert('', tkinter.END, values=i)
                else:
                    self.msgBox = messagebox.showinfo('Produto não encotrado', 'O Produto não foi encontrado.')
        elif(enc != ''):
            lista = cdb.Lists.produto_encomenda(self, 'CODIGO', enc)
            if type(lista) is list:
                if len(lista) > 0:
                    lista = list(lista[0]) 
                    if(lista[1] != ''):     #Verifica se o Pet já está disponível na Encomenda.
                        lista2 = cdb.Lists.produto_pet(self, 'CODIGO', lista[1])    #Busca os dados do pet que está disponível na encomenda
                        lista2 = list(lista2[0])
                        #Constroi uma lista com dados expecíficos das lista anteriores
                        lista3 = []
                        lista3.insert(0, lista[0])
                        lista3.insert(1, "Encomenda")
                        lista3.insert(2, lista2[1])
                        lista3.insert(3, lista2[2])
                        lista3 = [lista3]
                        for i in lista3:
                            self.lista_venda_1.insert('', tkinter.END, values=i)
                    else:
                        self.msgBox = messagebox.showinfo('Pet indisponível', 'O Pet desta encomenda ainda não está disponível.') #Retorna uma mensagem caso o pet da encomenda ainda não entá disponível
                else:
                    self.msgBox = messagebox.showinfo('Produto não encotrado', 'O Produto não foi encontrado.')
        else:
            self.msgBox = messagebox.showinfo('Nenhum Produto Digitado', 'Digite o codigo do produto para adiciona-lo.')    #Retona uma mensagem caso nenhum código de produto ou encomenda seja digitado.
    except Exception as erro:
        # Se ocorrer alguma exceção também será retornado FALSE
        return 0       

#Função que calcula e insere o total da venda no capo total
def total_venda(self):
     # Aqui ocorre o tratamento de exceções
    try:
        valores = []
        for i in self.lista_venda_1.get_children():
            col1, col2, col3, col4 = self.lista_venda_1.item(i, 'values')
            valores.append(col4)
        valores = list(map(double, valores))
        clean_tabela_venda(self, 1)
        self.lista_venda_2.insert('', tkinter.END, values= sum(valores)) 
    # Caso ocorra alguma exceção seja tratada aqui
    except Exception as erro:
        # Se ocorrer alguma será retornado falso
        return 0
    
# Função auxiliar que mostra uma mensagem de erro
def show_erro(self, obj):
    self.msg = messagebox.showerror('Erro!', obj)

# Função auxiliar que mostra uma mensagem informativa
def show_info(self, obj):
    self.msg = messagebox.showinfo('OK', obj)

# Função auxiliar que mostra uma mensagem de confirmação
def show_ok(self, obj):
    self.msg = messagebox.askyesno('Confirma ?', obj)
    # Retorna o valor da confirmação, podendo ser verdadeiro, ou falso
    return self.msg