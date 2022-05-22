# -*- coding: utf-8 -*-

import sqlite3

class BD():
    def conecta_bd(self):
        self.conecta = sqlite3.connect("pet_shop.db")
        self.cursor = self.conecta.cursor(); print("Conectando")
        
    def desconecta_bd(self):
        self.conecta.close(); print("Desconectando")
             
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
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Clientes (
                CLI_CODIGO INTEGER(4) PRIMARY KEY,
                CLI__NOME CHAR(30) NOT NULL,
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