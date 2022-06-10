# Importa o módulo de popup de mensagens do tkinter
from contextlib import nullcontext
from email import message_from_string
from tkinter import messagebox
# Importa o módulo de exibição das telas
import frames as frames
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
    if(self.msgBox == 'yes'):
        self.et_Codigo_encomenda.delete(0, 'end')
        self.et_Codigo_cli.delete(0, 'end')
        self.et_Raca.delete(0, 'end')
        self.et_Sexo.delete(0, 'end')
        self.et_Idade.delete(0, 'end')
        self.et_Valor.delete(0, 'end')
        self.et_Codigo_pet.delete(0, 'end')

# Função que vai limpar os campos da tela de vendas
def clean_vendas(self):
    self.msgBox = messagebox.askyesno('Limpar os campos', 'Deseja realmente limpar os campos ?')
    if(self.msgBox == 'yes'):
        self.et_Codigo_produto.delete(0, 'end')
        self.et_Codigo_pet.delete(0, 'end')
        self.et_Codigo_encomenda.delete(0, 'end')

# Função que vai limpar os campos da tela de vendas de pet
def clean_venda_pet(self, opcao = 0):
    if(opcao == 0):
        self.msgBox = messagebox.askyesno('Limpar os campos', 'Deseja realmente limpar os campos ?')
        if(self.msgBox == True):
            self.et_Codigo_pet.delete(0, 'end')
            self.et_Codigo_dono.delete(0, 'end')
            self.et_Codigo_venda_pet.delete(0, 'end')
    elif(opcao == 1):
        self.et_Codigo_pet.delete(0, 'end')
    elif(opcao == 2):
        self.et_Codigo_dono.delete(0, 'end')

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