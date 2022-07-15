import sqlite3
import validador
import requests


class Tabelacliente:
    conexao = sqlite3.connect('exercicio.db')
    cursor = conexao.cursor()

    def __init__(self,nome, cpf, cep):
        self.nome = nome
        self.cpf = cpf
        self.cep = cep

    def execute(self):
        Tabelacliente.cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
        'id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE ,'
        'nome_cliente TEXT ,'
        'cpf_cliente TEXT UNIQUE ,'
        'cep_cliente TEXT ,'
        'cidade_cliente TEXT ,'
        'estado_cliente TEXT ,'
        'bairro_cliente TEXT,'
        'rua_cliente TEXT ,'
        'numero_cliente TEXT)')

        Tabelacliente.conexao.commit()


    def cadastrarcliente(self):

        alvo = f'https://cep.awesomeapi.com.br/{self.cep}'
        response = requests.get(alvo)
        response_json = response.json()

        if validador.validarcpf(self.cpf) == True and len(self.cep) == 8:

            Tabelacliente.cursor.execute('INSERT INTO clientes(nome_cliente,cpf_cliente, cep_cliente, cidade_cliente, estado_cliente, bairro_cliente, rua_cliente)'
                        'VALUES(?,?,?,?,?,?,?)', (self.nome, self.cpf, self.cep,response_json["city"], response_json["state"], response_json["district"],response_json["address"]))
        else:
            print("Informações de cadastro inválidas")
        

        Tabelacliente.conexao.commit()



        

    
    def editar_nome_cliente(self):
        novonome = input("Digite aqui o novo nome: ")
        id = input("Digite aqui o id: ")
        Tabelacliente.cursor.execute(f'UPDATE  clientes SET nome_cliente = "{novonome}" WHERE id="{id}"')
        Tabelacliente.conexao.commit()



    def editar_cpf_cliente(self):
        novocpf = input("Digite aqui o novo cpf: ")
        id = input("Digite aqui o id: ")
        Tabelacliente.cursor.execute(f'UPDATE  clientes SET cpf_cliente="{novocpf}" WHERE id="{id}"')
        Tabelacliente.conexao.commit() 


    def editar_cep_cliente(self):
        novocep = input("Digite aqui o novo cep: ")
        id = input("Digite aqui o id: ")
        Tabelacliente.cursor.execute(f'UPDATE  clientes SET cep_cliente= "{novocep}" WHERE id= "{id}"')
        Tabelacliente.conexao.commit()


gabriel = Tabelacliente("Andrietti", "12986007902", "89062140")
