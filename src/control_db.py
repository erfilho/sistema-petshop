# Importa o arquivo de controle do banco de dados
import backend as be
# Importa o arquivo de funções auxiliares
import func as aux
from tkinter import messagebox

class Controler():
    # Variável que tem os comandos do backend
    trans = be.TransactionObject()

    # Verifica a senha na hora do login
    def check_senha(self, _cpf, _senha):
        # Referencia a variável do objeto que se comunica com o banco de dados para organizar o código de forma mais limpa
        trans = self.trans
        # Ocorre o tratamento de excessões
        try:
            # Verifica se o cpf está de acordo com as especificações
            if aux.valida_cpf(_cpf):
                cpf = _cpf
            else:
                raise Exception('CPF inválido!')
            # Retorna os campos necessários para a validação do login na hora do login dos funcionários
            sql = f"""
                SELECT CARGO_FUN, NOME_FUN, CPF_FUN FROM Funcionarios
                WHERE CPF_FUN = '{cpf}' AND SENHA_FUN = '{_senha}'
            """
            # Cria a conexão com o banco de dados
            trans.connect()
            # Vai executar o comando SQL
            trans.execute(sql)
            # Retorna os registros encontrados seguindo o comando SQL
            lista = trans.fetchall()
            # Faz o commit dos dados para o banco de dados
            trans.persist()
            # Fecha a conexão com o banco de dados
            trans.disconnect()
            # Verifica se foi encontrado algum registro do usuário
            if len(lista) > 0:
                # Retorna os registros encontrados
                return lista
            else:
                raise Exception('CPF ou Senha incorretos, tente novamente!')
        # Caso ocorra alguma exceção sera tratado o esenharro aqui
        except Exception as erro:
            # Retorna uma mensagem com a causa do erro caso haja alguma exceção
            aux.show_erro(self, f'Erro verificação de login!\n{erro}')
    
    # Verifica a existência de cpfs duplicados na tabela clientes
    def check_cpf(cpf):
        # Vai ser retornada a pesquisa pelo campo CPF_CLI igual ao cpf, na tabela clientes, caso exista algum registro
        lista = be.search('Clientes', '*' ,'CPF_CLI', cpf)
        # Se a lista for maior que 0, significa que o cpf já está cadastado
        if len(lista) > 0:
            # Retorna 1, caso seja verdade do cpf já estar cadastrado
            return 1
        # Caso não exista nenhum registro com o mesmo valor do CPF, retorna 0
        return 0

    # Verifica a existência de códigos duplicados
    def check_cod(tabela, codigo):
        # Vai ser retornado o resultado da pesquisa na tabela pelo campo código se for igual ao valor do código
        lista = be.search(tabela, '*', 'CODIGO', codigo)
        # Se a lista for maior do que 0, irá significar que existe já um registro cadastrado com o mesmo código
        if len(lista) > 0:
            # Retorna 1 caso exista algum registro com o mesmo código
            return 1
        # Caso não exista, retorna 0
        return 0
    
    # Verifica a existência de códigos duplicados
    def verifica_encomenda(self, raca, sexo, idade, valor, codigo_pet):
        # Vai ser retornado o resultado da pesquisa na tabela pelo campo código se for igual ao valor do código
        lista = be.search_encomenda(raca, sexo, idade, valor)
        # Se a lista for maior do que 0, irá significar que existe já um registro cadastrado com o mesmo código
        if len(lista) > 0:
            # Retorna 1 caso exista algum registro com o mesmo código
            self.msg = messagebox.askyesno('Encomenda Pet', 'O pet recém cadastrado se encaixa nas exigências da Encomenda Código: %d\nGostaria de adiciona-lo a encomenda?' % lista[0])
            if(self.msg):
                lista = list(lista[0])
                be.add_pet_encomenda(lista[0], codigo_pet)
                return 1
            else:
                return 0
        # Caso não exista, retorna 0
        else:
            return 0

class Factory():
    # Variável da classe Controler que vai ser a conexão com o banco de dados
    controller = Controler

    # Fabrica de clientes
    def cliente_fac(self, codigo, nome, cpf, data_n, logradouro, cidade, bairro, uf, cel, email):
        # Referencia a varíável da classe controller para que fique um código mais limpo
        ctrl = self.controller
        # Ocorre o tratamento de exceções e a execução da tarefa principal da função
        try:
            # Atribui os valores validados as variaveis referentes
            codigo = aux.valida_cod(codigo)
            cpf = aux.valida_cpf(cpf)
            cel = aux.valida_cel(cel)
            email = aux.valida_email(email)

            # Tabela referente a função
            tabela = "Clientes"
            # Confirma se o usuário deseja realmente confirmar o cadastro
            if aux.show_ok(self, 'Deseja confirmar o cadastro ?') == False:
                # Caso o cliente não confirme será gerada uma exceção
                raise Exception('Cadastro cancelado!')
            # Verifica se os campos estão de acordo com as especificações
            if aux.valida_cod(codigo) == False:
                # Caso o código não esteja de acordo com as especificações será gerada uma exceção
                raise Exception('O código não está de acordo com as especificações!')
            elif aux.valida_cpf(cpf) == False:
                # Caso o cpf do cliente não esteja de acordo com as especificações será gerada uma exceção
                raise Exception('O CPF não está de acordo com as especificações!')
            elif aux.valida_cel(cel) == False:
                # Caso o celular do cliente não esteja de acordo com as especificações será gerada uma exceção
                raise Exception('O celular não está de acordo com as especificações!')
            elif aux.valida_email(email) == False:
                # Caso o email do cliente não esteja de acordo com as especificações será gerada uma exceção
                raise Exception('O Email não está de acordo com as especificações!')
            # Verifica se o código já está cadastrado
            elif ctrl.check_cod(tabela, codigo):
                # Caso o código já esteja cadastrado irá ser gerada uma exceção
                raise Exception("Código já cadastrado, tente novamente!")
            elif ctrl.check_cpf(cpf):
                # Caso o cpf já esteja cadastrado também irá ser gerada uma exceção
                raise Exception("CPF já cadastrado, tente novamente!")
            else:
                # Comando SQL que vai ser executado para a inserção na tabela acima
                sql = f"""
                    INSERT INTO {tabela} VALUES(
                        {codigo}, 
                        '{nome}', 
                        '{cpf}', 
                        '{data_n}', 
                        '{logradouro}', 
                        '{cidade}', 
                        '{bairro}', 
                        '{uf}',
                        '{cel}', 
                        '{email}' 
                    );
                """
                # Função que vai executar o comando em sql
                be.execute(sql)
                # Retorna uma mensagem de sucesso
                aux.show_info(self, f"Cliente {codigo}, cadastrado com sucesso!")
        # Caso ocorra alguma exceção irá ser tratada aqui
        except Exception as erro:
            # Retorna uma mensagem com a causa do erro
            aux.show_erro(self, f"Erro cadastro de clientes!\n {erro}")

    # Fabrica de produtos
    def produtos_fac(self, codigo, nome, preco):
        # Referencia a varíável da classe controller para que fique um código mais limpo
        ctrl = self.controller
        # Ocorre o tratamento de exceções e a execução da tarefa principal da função
        try:
            if(codigo != '' and nome != '' and preco != ''):
                # Tabela referente a função
                tabela = "Produtos"
                # Confirma se o usuário deseja realmente confirmar o cadastro
                if aux.show_ok(self, 'Deseja confirmar o cadastro ?') == False:
                    # Caso o cliente não confirme será gerada uma exceção
                    raise Exception('Cadastro cancelado!')
                # Verifica se os campos estão de acordo com as especificações
                elif aux.valida_cod(codigo) == False:
                    # Caso o código não esteja de acordo com as especificações será gerada uma exceção
                    raise Exception('Código inválido!')
                # Verifica se o código já está cadastrado
                elif ctrl.check_cod(tabela, codigo):
                    # Caso o código já esteja cadastrado irá ser gerada uma exceção
                    raise Exception("Código já cadastrado, tente novamente!")
                elif aux.Valida_preco(preco) == False:
                    # Caso o código já esteja cadastrado, irá ser gerada uma exceção
                    messagebox.showinfo('Preço inválido', 'Digite um preço de produto válido.')
                else:
                    # Comando SQL que vai ser utilizado para a inserção na tabela acima
                    sql = f"""
                        INSERT INTO {tabela} VALUES(
                            {codigo},
                            '{nome}',
                            '{preco}'
                        );
                    """
                    # Função que vai executar o comando em sql
                    be.execute(sql)
                    # Retorna uma mensagem de sucesso
                    aux.show_info(self, f"Produto {codigo}, cadastrado com sucesso!")
                    return True
            else:
                messagebox.showinfo('Campos vazios', 'Preencha os campos para prosseguir com o cadastro')
                return False
        # Caso ocorra alguma exceção irá ser tratada aqui
        except Exception as erro:
            # Retorna uma mensagem com a causa do erro
            aux.show_erro(self, f"Erro cadastro de produtos!\n{erro}")
            return False

    # Fabrica de pets de clientes
    def pet_cliente_fac(self, codigo, nome, idade, sexo, codigo_dono, raca):
        # Referencia a variável da classe controller para que fique um código mais limpo
        ctrl = self.controller
        # Ocorre o tratamento de exceções e a execução da tarefa principal da função
        try:
            # Tabela referente a função
            tabela = "PetCliente"
            # Verifica se os campos estão de acordo com as especificações
            if aux.valida_cod(codigo) == False:
                # Caso o código não esteja de acordo com as especificações será gerada uma exceção
                raise Exception('Código inválido!')
            elif aux.valida_cod(codigo_dono) == False:
                # Caso o código não esteja de acordo com as especificações será gerada uma exceção
                raise Exception('Código de dono inválido!')
            # Verifica se o código já está cadastrado
            elif ctrl.check_cod(tabela, codigo):
                # Caso o código já esteja cadastrado irá ser gerada uma exceção
                raise Exception("Código já cadastrado, tente novamente!")
            elif ctrl.check_cod("Clientes", codigo_dono) == 0:
                    # Caso o código não esteja cadastrado, irá mostrar uma mensagem
                    messagebox.showinfo('Dono não encontrado', 'O dono não foi encontrado no banco de dados.')
            else:
                if (idade != ''):
                    if aux.Valida_idade_pet(idade) == False:
                        # Caso o código já esteja cadastrado, irá ser gerada uma exceção
                        messagebox.showinfo('Idade inválida', 'Digite uma idade de pet válida.')
                    else:
                        # Comando SQL que vai ser utilizado para a inserção na tabela acima
                        sql = f"""
                            INSERT INTO {tabela} VALUES (
                                {codigo},
                                '{nome}',
                                '{idade}',
                                '{sexo}',
                                '{raca}',
                                '{codigo_dono}'
                            );
                        """
                        # Função que vai executar o comando em sql
                        be.execute(sql)
                        # Retorna uma mensagem de sucesso
                        aux.show_info(self, f"Pet {codigo}, cadastrado com sucesso!")
                        return True
                else:
                    # Comando SQL que vai ser utilizado para a inserção na tabela acima
                    sql = f"""
                        INSERT INTO {tabela} VALUES (
                            {codigo},
                            '{nome}',
                            '{idade}',
                            '{sexo}',
                            '{raca}',
                            '{codigo_dono}'
                        );
                    """
                    # Função que vai executar o comando em sql
                    be.execute(sql)
                    # Retorna uma mensagem de sucesso
                    aux.show_info(self, f"Pet {codigo}, cadastrado com sucesso!")
                    return True
        # Caso ocorra alguma exceção irá ser tratada aqui
        except Exception as erro:
            # Retorna uma mensagem com a causa do erro
            aux.show_erro(self, f"Erro cadastro de pets!\n {erro}")
            return False

    # Fabrica de pets para vendas
    def pet_venda_fac(self, codigo, nome, idade, sexo, raca, preco):
        # Referencia a variável da classe controller para que fique um código mais limpo
        ctrl = self.controller
        # Ocorre o tratamento de exceções e a execução da tarefa principal da função
        try:
            # Tabela referente a função
            tabela = "PetVenda"
            # Verifica se os campos estão de acordo com as especificações
            if aux.valida_cod(codigo) == False:
                raise Exception('Código inválido!')
            # Verifica se o código já está cadastrado
            elif ctrl.check_cod(tabela, codigo):
                # Caso o código já esteja cadastrado irá ser gerada uma exceção
                raise Exception("Código já cadastrado, tente novamente!")
            elif aux.Valida_preco(preco) == False:
                    # Caso o código já esteja cadastrado, irá ser gerada uma exceção
                    messagebox.showinfo('Valor inválido', 'Digite um valor máximo de pet válido.')
            elif aux.Valida_sexo_pet(sexo) == False:
                # Caso o código já esteja cadastrado, irá ser gerada uma exceção
                messagebox.showinfo('Sexo inválido', 'Utilize F para Feminino ou M para Masculino')
            else:
                if(idade != ''):
                    if aux.Valida_idade_pet(idade) == False:
                        # Caso o código já esteja cadastrado, irá ser gerada uma exceção
                         messagebox.showinfo('Idade inválido', 'Digite uma idade de pet válida.')
                    else:
                        sql = f"""
                            INSERT INTO {tabela} VALUES (
                                {codigo},
                                '{nome}',
                                '{idade}',
                                '{sexo}',
                                '{raca}',
                                '{preco}'
                            );
                        """
                        # Função que vai executar o comando em sql
                        be.execute(sql)
                        # Retorna uma mensagem de sucesso
                        aux.show_info(self, f"Pet {codigo}, cadastrado com sucesso!")
                        Controler.verifica_encomenda(self, raca, sexo, idade, preco, codigo)
                        return True
                else:
                    sql = f"""
                            INSERT INTO {tabela} VALUES (
                                {codigo},
                                '{nome}',
                                '{idade}',
                                '{sexo}',
                                '{raca}',
                                '{preco}'
                            );
                        """
                    # Função que vai executar o comando em sql
                    be.execute(sql)
                    # Retorna uma mensagem de sucesso
                    aux.show_info(self, f"Pet {codigo}, cadastrado com sucesso!")
                    Controler.verifica_encomenda(self, raca, sexo, idade, preco, codigo)
                    return True

        # Caso ocorra alguma exceção irá ser tratada aqui
        except Exception as erro:
            # Retorna uma mensagem com a causa do erro
            aux.show_erro(self, f"Erro cadastro de pets!\n {erro}")
            return False

    # Fabrica de pets de dois tipos 
    def pet_fac(self, codigo, nome, idade, sexo, codigo_dono, raca, preco, checkbox):
        # Ocorre o tratamento de exceções e a execução da tarefa principal da função
        try:      
            if checkbox == 1:
                if(codigo != '' and raca != '' and preco!= ''):
                    # Confirma se o usuário deseja realmente confirmar o cadastro
                    if aux.show_ok(self, 'Deseja confirmar o cadastro ?') == False:
                    # Caso o cliente não confirme será gerada uma exceção
                        raise Exception('Cadastro cancelado!')
                    else:
                        retorno = self.pet_venda_fac(codigo, nome, idade, sexo, raca, preco)
                        return retorno
                else:
                    messagebox.showinfo('Campos vazios', 'Existem campos obrigatórios não preenchidos, verifique os dados.')
                    return False
            else:
                if(codigo != '' and raca != '' and codigo_dono != ''):
                    if aux.show_ok(self, 'Deseja confirmar o cadastro ?') == False:
                        # Caso o cliente não confirme será gerada uma exceção
                        raise Exception('Cadastro cancelado!')
                    else:
                        retorno = self.pet_cliente_fac(codigo, nome, idade, sexo, codigo_dono, raca)
                        return retorno
                else:
                    messagebox.showinfo('Campos vazios', 'Existem campos obrigatórios não preenchidos, verifique os dados.')
                    return False
        # Caso ocorra alguma exceção será tratada aqui
        except Exception as erro:
            # Retorna uma mensagem com a causa do erro
            aux.show_erro(self, f'Erro no cadastro de pets!\n{erro}')
            return False

    # Fabrica de encomendas
    def encomenda_fac(self, codigo, codigo_cli, raca, sexo, idade, valor, pet):
        
        # Referencia a variável da classe controller para que fique um código mais limpo
        ctrl = self.controller
        # Ocorre o tratamento de exceções e a execução da tarefa principal da função
        try:
            if(codigo != '' and codigo_cli != '' and raca != '' and idade != '' and valor !=''):
                # Tabela referente a função
                tabela = 'EncomendaPet'
                # Confirma se o usuário deseja confirmar o cadastro
                if aux.show_ok(self, 'Deseja confirmar o cadastro ?') == False:
                    raise Exception('Cadastro cancelado!')
                # Verifica se os campos estão de acordo com as especificações
                elif aux.valida_cod(codigo) == False:
                    raise Exception('Código inválido!')
                elif aux.valida_cod(codigo_cli) == False:
                    raise Exception('Código de cliente inválido!')
                # Verifica se o código já está cadastrado
                elif ctrl.check_cod("Clientes", codigo_cli) == 0:
                    # Caso o código não esteja cadastrado, irá mostrar uma mensagem
                    messagebox.showinfo('Cliente não encontrado', 'O Cliente não foi encontrado no banco de dados.')
                elif ctrl.check_cod(tabela, codigo) == 1:
                    # Caso o código não esteja cadastrado, irá mostrar uma mensagem
                    messagebox.showinfo('Codigo de encomenda duplicado', 'Uma encomenda com o mesmo código já existe no banco.')
                elif aux.Valida_sexo_pet(sexo) == False:
                    # Caso o código já esteja cadastrado, irá ser gerada uma exceção
                    messagebox.showinfo('Sexo inválido', 'Utilize F para Feminino ou M para Masculino')
                elif aux.Valida_idade_pet(idade) == False:
                    # Caso o código já esteja cadastrado, irá ser gerada uma exceção
                    messagebox.showinfo('Idade inválida', 'Digite uma idade de pet válida.')
                elif aux.Valida_preco(valor) == False:
                    # Caso o código já esteja cadastrado, irá ser gerada uma exceção
                    messagebox.showinfo('Valor inválido', 'Digite um valor máximo de pet válido.')
                else:
                    # Comando SQL que vai ser executado para a inserção na tabela acima
                    sql = f"""
                        INSERT INTO {tabela} VALUES (
                            {codigo},
                            {codigo_cli},
                            '{raca}',
                            '{sexo}',
                            '{idade}',
                            '{valor}',
                            '{pet}'
                        );
                    """
                    # Função que vai executar o comando em sql
                    be.execute(sql)
                    # Retorna uma mensagem de sucesso
                    aux.show_info(self, f"Encomenda {codigo}, cadastrada com sucesso!")
                    return True
            else:
                messagebox.showinfo('Campos vazios', 'Existem campos obrigatórios não preenchidos, verifique os dados.') 
                return False
        # Caso ocorra alguma exceção será tratada aqui
        except Exception as erro:
            # Retorna uma mensagem com a causa do erro
            aux.show_erro(self, f"Erro cadastro de encomendas!\n{erro}")
            return False

    # Fabrica de vendas de pets
    def vendaPet_fac(self, codigo, codigo_pet, codigo_cli):
        # Referencia a variável da classe controller para que fique um código mais limpo
        ctrl = self.controller
        # Aqui ocorre o tratamento de exceções e a execução da tarefa principal
        try:
            if(codigo != '' and codigo_pet != '' and codigo_cli != ''):
                # Tabela referente a função
                tabela = "VendaPet"
                # Confirma se o usuário deseja salvar o cadastro
                if aux.show_ok(self, 'Deseja confirmar o cadastro ?') == False:
                    return 0
                # Verifica se os campos estão de acordo com as especificações
                elif aux.valida_cod(codigo) == False:
                    # Lança uma exceção se o código da venda estiver inválido
                    raise Exception('Código de venda inválido!')
                elif aux.valida_cod(codigo_pet) == False:
                    # Lança uma exceção se o código do pet estiver inválido
                    raise Exception('Código de pet inválido!')
                elif aux.valida_cod(codigo_cli) == False:
                    # Lança uma exceção se o codigo de cliente estiver inválido
                    raise Exception('Código do cliente inválido!')
                # Verifica os codigos estão presentes no banco.
                elif ctrl.check_cod("PetVenda", codigo_pet) == 0:
                    #se não existir, mostra uma mensagem
                    messagebox.showinfo('Pet não encontrado', 'O Pet não foi encontrado no banco de dados.')
                elif ctrl.check_cod("Clientes", codigo_cli) == 0:
                    messagebox.showinfo('Cliente não encontrado', 'O Cliente não foi encontrado no banco de dados.')
                elif ctrl.check_cod(tabela, codigo) == 1:
                    messagebox.showinfo('Codigo de venda duplicado', 'Uma venda com mesmo código de venda já existe no banco.')
                
                # Caso esteja tudo correto, será executada a tarefa principal da função
                else:
                    # Comando SQL que vai ser executado para a inserção na tabela acima
                    sql = f"""
                        INSERT INTO {tabela} VALUES(
                            {codigo},
                            {codigo_cli},
                            {codigo_pet}
                        );
                    """
                    # Função que vai executar o comando em sql\
                    be.execute(sql)
                    # Retorna uma mensagem de sucesso
                    aux.show_info(self, f'Venda {codigo}, cadastrada com sucesso!')
                    return True
            else:
                messagebox.showinfo('Campos vazios', 'Preencha os campos para prosseguir com a venda')
                return False
        # Caso ocorra alguma exceção será tratada aqui
        except Exception as erro:
            # Retorna uma mensagem com a causa do erro
            aux.show_erro(self, f"Erro no cadastro de vendas!\n{erro}")
            return False

# Classe que vai retornar os dados necessários para algumas aplicações
class Lists():
    # Função que vai retornar a lista dos clientes
    def clientes_list(self):
        # Ocorrerá o tratamento de exceções
        try:
            # Tabela que vai ser feita a pesquisa
            tabela = 'Clientes'
            # Campos que vão ser retornados na pesquisa
            campos = 'CODIGO, NOME_CLI, CELULAR_CLI'
            # Retorna os registros encontrados na pesquisa feita utilizada a função
            lista = be.search(tabela, campos, None, None)
            # Irá retornar os registros encontrados
            return lista
        # Caso ocorra um erro, vai ser tratado aqui
        except Exception as erro:
            # Caso ocorra uma exceção, vai ser retornada a causa do erro
            aux.show_erro(f"Erro!\n {erro}")
    
    # Função que vai retornar a lista dos pets disponíveis para a venda
    def pets_venda_list(self):
        # Ocorrerá o tratamento de exceções
        try:
            # Tabela que vai ser feita a pesquisa
            tabela = 'PetVenda'
            # Campos que vão ser retornados na pesquisa
            # Correção de erro, retornando mais dados do que o necessário
            campos = 'CODIGO, IDADE_PET, SEXO_PET, RACA_PET, PRECO_PET'
            # Retorna os registros encontrados na pesquisa feita utilizada a função
            lista = be.search(tabela, campos, None, None)
            # Irá retornar os registros encontrados
            return lista
        # Caso ocorra um erro, vai ser tratado aqui
        except Exception as erro:
            # Caso ocorra uma exceção, vai ser retornada a causa do erro
            aux.show_erro(f"Erro!\n {erro}")
    
    # Função que vai retornar o produto
    def produto_comum(self, campo, valor):
        # Ocorrerá o tratamento de exceções
        try:
            # Tabela que vai ser feita a pesquisa
            tabela = 'Produtos'
            # Campos que vão ser retornados na pesquisa
            # Correção de erro, retornando mais dados do que o necessário
            campos = 'CODIGO, NOME_PROD, PRECO_PROD'
            # Retorna os registros encontrados na pesquisa feita utilizada a função
            lista = be.search(tabela, campos, campo, valor)
            # Irá retornar os registros encontrados
            return lista
        # Caso ocorra um erro, vai ser tratado aqui
        except Exception as erro:
            # Caso ocorra uma exceção, vai ser retornada a causa do erro
            aux.show_erro(f"Erro!\n {erro}")
    
    # Função que vai retornar o pet
    def produto_pet(self, campo, valor):
        # Ocorrerá o tratamento de exceções
        try:
            # Tabela que vai ser feita a pesquisa
            tabela = 'PetVenda'
            # Campos que vão ser retornados na pesquisa
            # Correção de erro, retornando mais dados do que o necessário
            campos = 'CODIGO, NOME_PET, PRECO_PET'
            # Retorna os registros encontrados na pesquisa feita utilizada a função
            lista = be.search(tabela, campos, campo, valor)
            # Irá retornar os registros encontrados
            return lista
        # Caso ocorra um erro, vai ser tratado aqui
        except Exception as erro:
            # Caso ocorra uma exceção, vai ser retornada a causa do erro
            aux.show_erro(f"Erro!\n {erro}")
    
    # Função que vai retornar o pet
    def produto_venda_pet(self, campo, valor):
        # Ocorrerá o tratamento de exceções
        try:
            # Tabela que vai ser feita a pesquisa
            tabela = 'VendaPet'
            # Campos que vão ser retornados na pesquisa
            # Correção de erro, retornando mais dados do que o necessário
            campos = 'CODIGO, CODIGO_PET'
            # Retorna os registros encontrados na pesquisa feita utilizada a função
            lista = be.search(tabela, campos, campo, valor)
            # Irá retornar os registros encontrados
            return lista
        # Caso ocorra um erro, vai ser tratado aqui
        except Exception as erro:
            # Caso ocorra uma exceção, vai ser retornada a causa do erro
            aux.show_erro(f"Erro!\n {erro}")
    
    # Função que vai retornar a encomenda
    def produto_encomenda(self, campo, valor):
        # Ocorrerá o tratamento de exceções
        try:
            # Tabela que vai ser feita a pesquisa
            tabela = 'EncomendaPet'
            # Campos que vão ser retornados na pesquisa
            # Correção de erro, retornando mais dados do que o necessário
            campos = 'CODIGO, PET_ENC'
            # Retorna os registros encontrados na pesquisa feita utilizada a função
            lista = be.search(tabela, campos, campo, valor)
            # Irá retornar os registros encontrados
            return lista
        # Caso ocorra um erro, vai ser tratado aqui
        except Exception as erro:
            # Caso ocorra uma exceção, vai ser retornada a causa do erro
            aux.show_erro(f"Erro!\n {erro}")