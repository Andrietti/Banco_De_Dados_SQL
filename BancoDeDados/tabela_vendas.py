import sqlite3
import datetime
from tabela_clientes import *

hoje = datetime.date.today()



class Tabelavendas():
    conexao = sqlite3.connect('exercicio.db')
    cursor = conexao.cursor()

    def __init__(self, codigo_b_p, cpf_cliente ,quantidade, valor_unitario):
        self.data = hoje
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.codigo_b_p = codigo_b_p
        self.cpf_cliente = cpf_cliente
    
    def execute(self):
        Tabelavendas.cursor.execute('CREATE TABLE IF NOT EXISTS vendas('
        'id_tabelavendas INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE ,'
        'data_da_venda TEXT,'
        'cod_de_barras TEXT,'
        'cpf_cliente TEXT,'
        'quantidade REAL,'
        'valor_unitario FLOAT,'
        'valor_total FLOAT)')

        Tabelavendas.conexao.commit()
    


    def cadastrarvenda(self):
        Tabelavendas.cursor.execute('INSERT INTO vendas(data_da_venda, cod_de_barras, cpf_cliente, quantidade, valor_unitario, valor_total)'
        'VALUES(?,?,?,?,?,?)', (self.data, self.codigo_b_p ,self.cpf_cliente, self.quantidade, self.valor_unitario, self.quantidade * self.valor_unitario))
        Tabelavendas.conexao.commit()


    def alterar_quantidade(self, quantidade, cod):
        quantidade = input("Digite aqui a nova quantidade do produto: ")
        cod = input("Digite aqui o codigo do produto:  ")

        Tabelavendas.cursor.execute(f'UPDATE vendas SET quantidade="{quantidade}" WHERE cod_barras = "{cod}"')



    def alterar_valor_unitario(self, valor_unitario, cod):
        valor_unitario = input("Digite aqui o novo valor unitario do produto: ")
        cod = input("Digite aqui o cidog do produto: ")
        Tabelavendas.cursor.execute(f'UPDATE valor_unitario SET valor_unitario="{valor_unitario}" WHERE cod_barras = "{cod}"')
    
