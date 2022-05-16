# -*- coding: utf-8 -*-

import sqlite3

class BD():
    def conecta_bd(self):
        self.conecta = sqlite3.connect("pet_shop.db")
        self.cursor = self.conecta.cursor(); print("Conectando")
        
    def desconecta_bd(self):
        self.conecta.close(); print("Desconectando")
        
    def dados(self, senha, cpf):
        print(senha, cpf)
        
    def AllData(self):
        BD.conecta_bd(self)
        
        self.cursor.execute("""
                    SELECT * FROM Funcionarios;
                    """)

        for linha in self.cursor.fetchall():
            print(linha)
            
        BD.desconecta_bd(self)
        
    def verifica_senha(self, cpf, senha):
        BD.conecta_bd(self)
        
        self.cursor.execute(""" SELECT FUN_CARGO, FUN_NOME, FUN_CPF FROM Funcionarios
                                WHERE FUN_CPF == (?) AND FUN_SENHA = (?);""", (cpf, senha))

        lista = self.cursor.fetchall()

        BD.desconecta_bd(self)
        return lista
