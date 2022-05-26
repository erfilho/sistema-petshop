# -*- coding: utf-8 -*-

import sqlite3
import os
from tkinter import *
from tkinter import messagebox
from pathlib import Path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class BD():
    def conecta_bd(self):
        self.conecta = sqlite3.connect(Path(ROOT_DIR, "pet_shop.db"))
        self.cursor = self.conecta.cursor();
        print("Conectando")
        
    def desconecta_bd(self):
        self.conecta.close()
        print("Desconectando")

    # Mod by Erineldo 26/05
    # Função para verificar a existência de registros duplicados
    def verifica_Codigos(self, codigo, tipo):
        BD.conecta_bd(self)
        if(tipo == 'clientes'):
            self.cursor.execute("""
                SELECT * FROM Clientes
            ;""")
            self.conecta.commit()
        elif(tipo == 'pets_vendas'):
            self.cursor.execute("""
                SELECT * FROM PetVenda
            ;""")
            self.conecta.commit()
        elif(tipo == 'pets_clientes'):
            self.cursor.execute("""
                SELECT * FROM PetCliente
            ;""")
            self.conecta.commit()
        elif(tipo == 'produtos'):
            self.cursor.execute("""
                SELECT * FROM Produtos
            ;""")
            self.conecta.commit()
        else: 
            return 0
        lista = self.cursor.fetchall()
        BD.desconecta_bd(self)
        for i in lista:
            if(i[0] == int(codigo)):
                return 1
    
    # Added by Erineldo 26/05
    # Função que verifica se existe algum cpf duplicado na hora do cadastro de clientes
    def verifica_cpf(self, cpf):
        BD.conecta_bd(self)
        self.cursor.execute("""
            SELECT CLI_CPF FROM Clientes
        ;""")
        self.conecta.commit()
        lista = self.cursor.fetchall()
        ret = 0
        for i in lista:
            if(i[0] == int(cpf)):
                ret = 1
        BD.desconecta_bd(self)
        return ret
             
    def verifica_senha(self, cpf, senha):
        BD.conecta_bd(self)
        
        self.cursor.execute(""" SELECT FUN_CARGO, FUN_NOME, FUN_CPF FROM Funcionarios
                                WHERE FUN_CPF == (?) AND FUN_SENHA = (?);""", (cpf, senha))

        lista = self.cursor.fetchall()
        BD.desconecta_bd(self)
        return lista

    def monta_produto(self):
        BD.conecta_bd(self)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS  Produtos (
                PROD_CODIGO INTEGER PRIMARY KEY,
                PROD_NOME CHAR(40) NOT NULL,
                PROD_PRECO REAL 
            );    
        """)
        self.conecta.commit()
        BD.desconecta_bd(self)
    
    def monta_pet_venda(self):
        BD.conecta_bd(self)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS  PetVenda (
                PET_V_CODIGO INTEGER(4) PRIMARY KEY,
                PET_V_NOME CHAR(30) NOT NULL,
                PET_V_IDADE INTEGER(3), 
                PET_V_SEXO CHAR(1),
                PET_V_RACA CHAR(30) NOT NULL,
                PET_V_PRECO REAL NOT NULL 
            );    
        """)
        self.conecta.commit()
        BD.desconecta_bd(self)
        
    def monta_pet_cliente(self):
        BD.conecta_bd(self)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS  PetCliente (
                PET_C_CODIGO INTEGER(4) PRIMARY KEY,
                PET_C_NOME CHAR(30) NOT NULL,
                PET_C_IDADE INTEGER(3), 
                PET_C_SEXO CHAR(1),
                PET_C_RACA CHAR(30) NOT NULL,
                PET_C_CODIGO_DONO REAL INTEGER(4) NOT NULL    
            );    
        """)
        self.conecta.commit()
        BD.desconecta_bd(self) 
        
    def monta_cliente(self):
        BD.conecta_bd(self)
        # Mod by Erinedo 24/05
        # Correção ortográfica - CLI__NOME -> CLI_NOME 
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Clientes (
                CLI_CODIGO INTEGER(4) PRIMARY KEY,
                CLI_NOME CHAR(30) NOT NULL,
                CLI_CPF INTEGER(11) NOT NULL,
                CLI_DATA_NASCIMENTO INTEGER(8), 
                CLI_LOGRADOURO CHAR(30),
                CLI_CIDADE CHAR(30),
                CLI_BAIRRO CHAR(30),   
                CLI_UF CHAR(2),
                CLI_CELULAR INTEGER(11) NOT NULL,
                CLI_EMAIL CHAR(30) NOT NULL
            );    
        """)
        self.conecta.commit()
        BD.desconecta_bd(self)

    def monta_venda_pets(self):
        BD.conecta_bd(self)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS VendaPet (
                VEND_CODIGO INTEGER(4) PRIMARY KEY,
                VEND_CODIGO_DONO INTEGER(4) NOT NULL,
                VEND_CODIGO_PET INTERGER(4) NOT NULL   
            );    
        """)
        self.conecta.commit()
        BD.desconecta_bd(self)
        
    def monta_encomenda_pet(self):
        BD.conecta_bd(self)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS EncomendaPet (
                ENC_CODIGO INTEGER(4) PRIMARY KEY,
                ENC_CODIGO_CLIENTE CHAR(30) NOT NULL,
                ENC_RACA INTEGER(11) NOT NULL,
                ENC_SEXO INTEGER(8), 
                ENC_IDADE CHAR(30),
                ENC_VALOR CHAR(30),
                ENC_PET CHAR(30)  
            );    
        """)
        self.conecta.commit()
        BD.desconecta_bd(self) 

    # Mod by Erineldo 26/05
    # Função para cadastro de clientes
    def cad_cliente(self, codigo, nome, cpf, data_n, logradouro, cidade, bairro, uf, cel, email):
        # Verifica se já existe um cliente cadastrado com o mesmo código
        if(BD.verifica_Codigos(self, codigo, 'clientes')):
            self.msgErro = messagebox.showerror('ERRO', 'Código já cadastrado.\n      Tente novamente.')
        else:
            if(BD.verifica_cpf(self, cpf)):
                self.msgErro = messagebox.showerror('ERRO', 'CPF já cadastrado.\n     Tente novamente.')
            else:
                BD.conecta_bd(self)
                self.cursor.execute("""
                    INSERT INTO Clientes VALUES(
                        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                    )   
                ;""", (codigo, nome, cpf, data_n, logradouro, cidade, bairro, uf, cel, email))
                self.conecta.commit()
                BD.desconecta_bd(self)

    # Mod by Erineldo 26/05
    # Inserção de produtos
    def cad_produto(self, codigo, nome, preco):
        # Veridica se já existe um produto cadastrado com o mesmo código
        cnt = BD.verifica_Codigos(self, codigo, 'produtos')
        if(cnt):  
            self.msgErro = messagebox.showerror('ERRO', 'Código já cadastrado.\n     Tente novamente.')
        else:
            BD.conecta_bd(self)
            self.cursor.execute("""
                INSERT INTO Produtos (PROD_CODIGO, PROD_NOME, PROD_PRECO)
                VALUES (
                    ?, ?, ?
                );
            """, (codigo, nome, preco))
            self.conecta.commit()  
            BD.desconecta_bd(self)

    # Mod by Erineldo 25/05
    # Função para cadastro de pets
    def cad_pet(self, codigo, nome, idade, sexo, codigo_dono, raca, preco, checkbox):
        if(checkbox == 1):
            # Verifica se já existe um pet para venda cadastrado com o mesmo código
            cnt = BD.verifica_Codigos(self, codigo, 'pets_vendas')
            if(cnt):
                self.msgErro = messagebox.showerror('ERRO', 'Código já cadastrado.\n     Tente novamente.')
            else:
                BD.conecta_bd(self)
                self.cursor.execute("""
                    INSERT INTO PetVenda
                    VALUES (
                        ?, ?, ?, ?, ?, ?
                    );
                """, (codigo, nome, idade, sexo, raca, preco))
                self.conecta.commit()
                BD.desconecta_bd(self)
        else:
            # Verifica se já existe um pet de cliente cadastrado com o mesmo código
            cnt = BD.verifica_Codigos(self, codigo, 'pets_clientes')
            if(cnt):
                self.msgErro = messagebox.showerror('ERRO', 'Código já cadastrado.\n     Tente novamente.')
            else:
                self.cursor.execute("""
                    INSERT INTO PetCliente
                    VALUES (
                        ?, ?, ?, ?, ?, ?
                    )
                """, (codigo, nome, idade, sexo, raca, codigo_dono))
                self.conecta.commit()
                BD.desconecta_bd(self)

    # Added by Erineldo - 24/05
    # Função para listar os pets
    def teste_Pets(self):
        BD.conecta_bd(self)
        self.cursor.execute("""
            SELECT * FROM PetVenda;
        """)
        listagem = self.cursor.fetchall()
        print(listagem)
        self.cursor.execute("""
            SELECT * FROM PetCliente;
        """)
        self.conecta.commit()
        listagem = self.cursor.fetchall()
        print(listagem)
        BD.desconecta_bd(self)

    # Added by Erineldo - 26/05
    # Função para listar os clientes
    def teste_Clientes(self):
        BD.conecta_bd(self)
        self.cursor.execute("""
            SELECT * FROM Clientes
        """)
        self.conecta.commit()
        listagem = self.cursor.fetchall()
        print(listagem)
        BD.desconecta_bd(self)

    # Added by Erineldo - 26/05
    # Função para listar os produtos
    def teste_Produtos(self):
        BD.conecta_bd(self)
        self.cursor.execute("""
            SELECT * From Clientes
        """)
        self.conecta.commit()
        listagem = self.cursor.fetchall()
        print(listagem)
        BD.desconecta_bd(self)