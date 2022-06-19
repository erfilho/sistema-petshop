import os
import sqlite3 as sql
from pathlib import Path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class TransactionObject():
    database  = Path(ROOT_DIR, 'database.db')
    conn      = None
    cur       = None
    connected = False

    # Vai realizar a conexão com banco de dados
    def connect(self):
        TransactionObject.conn    = sql.connect(TransactionObject.database)
        TransactionObject.cur     = TransactionObject.conn.cursor()
        TransactionObject.connected = True
        print('Conectando')
    # Vai fechar a conexão com o banco de dados
    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.connected = False
        print('Desconectando')
    # Vai executar um comando sql recebendo três parâmetros
    # - Self, referencia o próprio objeto
    # - sql, comando sql que vai ser executado
    # - params, vetor com os comandos sql que pode ser omitido
    def execute(self, sql, params = None):
        if TransactionObject.connected:
            print('Executando')
            if params == None:
                TransactionObject.cur.execute(sql)
            else:
                TransactionObject.cur.execute(sql, params)
            return True
        else:
            return False
    # Vai recuperar os valores recebidos de um comando select
    def fetchall(self):
        print('Concluindo op.')
        return TransactionObject.cur.fetchall()
    # Vai realizar o cmmit das operações realizadas
    def persist(self):
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        else:
            return False

# Função que vai inicializar o banco de dados na primeira execução
def initDB():
    trans = TransactionObject()
    sql_tabela_Produtos = """
        CREATE TABLE IF NOT EXISTS  Produtos (
            CODIGO INTEGER PRIMARY KEY,
            NOME_PROD CHAR(40) NOT NULL,
            PRECO_PROD REAL 
        ); 
    """
    sql_tabela_Pet_venda = """
        CREATE TABLE IF NOT EXISTS  PetVenda (
            CODIGO INTEGER(4) PRIMARY KEY,
            NOME_PET CHAR(30) NOT NULL,
            IDADE_PET INTEGER(3), 
            SEXO_PET CHAR(1),
            RACA_PET CHAR(30) NOT NULL,
            PRECO_PET REAL NOT NULL 
        );
    """
    sql_tabela_Pet_cliente = """
        CREATE TABLE IF NOT EXISTS  PetCliente (
            CODIGO INTEGER(4) PRIMARY KEY,
            NOME_PET CHAR(30) NOT NULL,
            IDADE_PET INTEGER(3), 
            SEXO_PET CHAR(1),
            RACA_PET CHAR(30) NOT NULL,
            CODIGO_DONO REAL INTEGER(4) NOT NULL 
        );
    """
    sql_tabela_Cliente = """
        CREATE TABLE IF NOT EXISTS Clientes (
            CODIGO INTEGER(4) PRIMARY KEY,
            NOME_CLI CHAR(30) NOT NULL,
            CPF_CLI INTEGER(11) NOT NULL,
            DATA_NASC_CLI INTEGER(8), 
            LOGRADOURO_CLI CHAR(30),
            CIDADE_CLI CHAR(30),
            BAIRRO_CLI CHAR(30),   
            UF_CLI CHAR(2),
            CELULAR_CLI INTEGER(11) NOT NULL,
            EMAIL_CLI CHAR(30) NOT NULL
        );
    """
    sql_tabela_Venda_pet = """
        CREATE TABLE IF NOT EXISTS VendaPet (
            CODIGO INTEGER(4) PRIMARY KEY,
            CODIGO_DONO INTEGER(4) NOT NULL,
            CODIGO_PET INTERGER(4) NOT NULL   
        );    
    """
    sql_tabela_Encomenda_pet = """
        CREATE TABLE IF NOT EXISTS EncomendaPet (
            CODIGO INTEGER(4) PRIMARY KEY,
            CODIGO_CLI CHAR(30) NOT NULL,
            RACA_ENC INTEGER(11) NOT NULL,
            SEXO_ENC INTEGER(8), 
            IDADE_EC CHAR(30),
            VALOR_ENC CHAR(30),
            PET_ENC CHAR(30)  
        );    
    """

    sql_tabela_Funcionarios = """
        CREATE TABLE IF NOT EXISTS Funcionarios(
            "CODIGO"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "NOME_FUN"	TEXT NOT NULL,
            "CPF_FUN"	TEXT NOT NULL,
            "CARGO_FUN"	TEXT NOT NULL,
            "SENHA_FUN"	TEXT NOT NULL
        );
    """
    trans.connect()
    try:
        trans.execute(sql_tabela_Produtos)
        trans.persist()
        trans.execute(sql_tabela_Pet_cliente)
        trans.persist()
        trans.execute(sql_tabela_Pet_venda)
        trans.persist()
        trans.execute(sql_tabela_Produtos)
        trans.persist()
        trans.execute(sql_tabela_Cliente)
        trans.persist()
        trans.execute(sql_tabela_Venda_pet)
        trans.persist()
        trans.execute(sql_tabela_Encomenda_pet)
        trans.persist()
        trans.execute(sql_tabela_Funcionarios)
        trans.persist()
    except Exception as erro:
        print(erro)

    trans.disconnect()

# Função que vai executar um script
def execute(sql):
    print('Executando')
    trans = TransactionObject()
    trans.connect()
    trans.execute(sql)
    trans.persist()
    trans.disconnect()

# Função que vai retornar todos os registros de alguma tabela
def view(tabela):
    trans = TransactionObject()
    trans.connect()
    sql = f"""
        SELECT * FROM {tabela}
    """
    trans.execute(sql)
    rows = trans.fetchall()
    trans.persist()
    trans.disconnect()
    return rows

# Função que vai retornar ma pesquis de uma encomenda que se encaixa em algum cadastro de pet
def search_encomenda(raca, sexo, idade, valor):
    trans = TransactionObject()
    if(sexo != ''):
        trans.connect()
        sql = f"""  
            SELECT CODIGO FROM EncomendaPet
                WHERE   
                RACA_ENC = '{raca}' AND
                (SEXO_ENC = '{sexo}' OR SEXO_ENC = '') AND
                IDADE_ENC >= '{idade}' AND
                VALOR_ENC >= '{valor}' AND
                PET_ENC = '';
        """
        trans.execute(sql)
    else:
        trans.connect()
    
        sql = f"""  
            SELECT CODIGO FROM EncomendaPet
                WHERE   RACA_ENC = '{raca}' AND
                SEXO_ENC = '' AND
                IDADE_ENC >= '{idade}' AND
                VALOR_ENC >= '{valor}' AND
                PET_ENC = '';
                    
            
        """
        trans.execute(sql)
    
    item = trans.fetchall()
    trans.persist()
    trans.disconnect()
    return item

# Função que vai retornar alguma pesquisa de uma tabela, recebendo o campo e o valor do campo
def search(tabela, src_campos = None, campo = None, valor = None):
    trans = TransactionObject()
    trans.connect()
    if src_campos == None and campo == None and valor == None:
        sql = f"""
            SELECT * FROM {tabela}
        """
        trans.execute(sql)
    elif src_campos != None and campo != None and valor != None:
        sql = f"""
            SELECT {src_campos} FROM {tabela}
            WHERE {campo} = '{valor}'
        """
        trans.execute(sql)
    elif src_campos != None and campo == None and valor == None:
        sql = f"""
            SELECT {src_campos} FROM {tabela}
        """
        trans.execute(sql)
    rows = trans.fetchall()
    trans.persist()
    trans.disconnect()
    return rows

# Função que vai deletar os códigos de alguma tabela
def delete(tabela, codigo = None):
    trans = TransactionObject()
    trans.connect()
    if codigo == None:
        sql = f"""
            DROP TABLE {tabela}
        """
        trans.execute(sql)
    else:
        sql = f"""
            DELETE FROM {tabela}
            WHERE codigo = '{codigo}'
        """
        trans.execute(sql)
    trans.persist()
    trans.disconnect()

#Função que vai adiconar pet a uma encomenda já existente no banco
def add_pet_encomenda(codigo_enc, codigo_pet):
    trans = TransactionObject()
    trans.connect()
    sql = f"""
        UPDATE  EncomendaPet 
        SET PET_ENC = '{codigo_pet}'
        WHERE CODIGO = '{codigo_enc}'
    """
    trans.execute(sql)
    trans.persist()
    trans.disconnect()

initDB()