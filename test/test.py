# Importa a biblioteca de testes
import unittest

# Importa bibliotecas necessárias para a importação de arquivos de pastas diferentes
import sys

# Configura a importação de bibliotecas de outras pastas
sys.path.insert(1, './src')

# Importa as bibliotecas com as funções
from func import *

class CpfTeste(unittest.TestCase):
    def teste_cpf_true(self):
        cpfs = ["001.222.333-44", "001.232.333-44"]
        for i in cpfs:
            self.assertTrue(valida_cpf(i), f"CPF{i}, não é válido!")

    def teste_cpf_false(self):
        cpfs = ['00122233344', '001222333-44', '001222333 44', '001 222 333 44']
        for i in cpfs:
            self.assertFalse(valida_cpf(i))

class CelTeste(unittest.TestCase):
    def teste_cel_true(self):
        cels = ['(88)91234-5555', '(11)91234-5555', '(00)12345-9090']
        for i in cels:
            self.assertTrue(valida_cel(i))

    def teste_cel_false(self):
        cels = ['8891234555', '88 9 1234 5555', '88 9 12345555']
        for i in cels:
            self.assertFalse(valida_cel(i))

class EmailTeste(unittest.TestCase):
    def teste_email_true(self):
        emails = ['fulano@gmail.com', 'fulano@gmail.com.br', 'fulano@bol.com.br']
        for i in emails:
            self.assertTrue(valida_email(i))
        
    def teste_email_false(self):
        emails = ['fulano@_.com', 'fulano@hot mail.com', 'fulano@bol.123']
        for i in emails:
            self.assertFalse(valida_email(i))

class CodTeste(unittest.TestCase):
    def teste_cod_true(self):
        cods = ['1234', '0001', '9999']
        for i in cods:
            self.assertTrue(valida_cod(i))
    
    def teste_cod_false(self):
        cods = ['abc1', '0 12', '01234', 'abcd']
        for i in cods:
            self.assertFalse(valida_cod(i))
            
class SexoTeste(unittest.TestCase):  
    def teste_sexo_true(self):   
        sexos = ['F', 'M', '']
        for i in sexos:
            self.assertTrue(valida_sexo_pet(i))
    def teste_sexo_false(self):
        sexos = ['a', '0', '01234', 'ab']        
        for i in sexos:
            self.assertFalse(valida_sexo_pet(i))
                
class PrecoTeste(unittest.TestCase):  
    def teste_preco_true(self):   
        precos = ['21', '131.45', '746']
        for i in precos:
            self.assertTrue(valida_preco(i))
    def teste_preco_false(self):
        precos = ['a', '0s', '012f4', 'a b']        
        for i in precos:
            self.assertFalse(valida_preco(i))
                                
class IdadeTeste(unittest.TestCase):  
    def teste_idade_true(self):   
        idade = ['21', '8', '100']
        for i in idade:
            self.assertTrue(valida_idade_pet(i))
    def teste_idade_false(self):
        idade = ['a', '0s', '012f4', 'a b']        
        for i in idade:
            self.assertFalse(valida_idade_pet(i))

class DataNascimentoTeste(unittest.TestCase):  
    def teste_dataNascimento_true(self):   
        data_nascimento = ['21/01/2002', '25/12/2010']
        for i in data_nascimento:
            self.assertTrue(valida_data_nascimento(i))
    def teste_dataNascimento_false(self):
        data_nascimento = ['a', '0s', '012f4', 'a b']        
        for i in data_nascimento:
            self.assertFalse(valida_data_nascimento(i))                                           

class UFTeste(unittest.TestCase):  
    def teste_uf_true(self):   
        uf = ['CE', 'MG']
        for i in uf:
            self.assertTrue(valida_UF(i))
    def teste_uf_false(self):
        uf = ['a', '0s', '012f4', 'a b', '00']        
        for i in uf:
            self.assertFalse(valida_UF(i))                                           
                        

if __name__ == "__main__":
    unittest.main()