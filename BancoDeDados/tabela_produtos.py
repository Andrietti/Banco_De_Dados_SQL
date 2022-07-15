import sqlite3


class Tabelaprodutos():

    conexao = sqlite3.connect('exercicio.db')
    cursor = conexao.cursor()

    def __init__(self, nome_p, familia_p, codigo_b_p):
        self.nome_p = nome_p
        self.familia_p = familia_p
        self.codigo_b_p = codigo_b_p



    def execute(self):        
        Tabelaprodutos.cursor.execute('CREATE TABLE IF NOT EXISTS produtos('
        'id_produtos INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE ,'
        'nome_produto TEXT ,'
        'familia_produto TEXT ,'
        
        'codigo_barras_produto TEXT)')
        Tabelaprodutos.conexao.commit()

    def cadastrarproduto(self):
    
        Tabelaprodutos.cursor.execute('INSERT INTO produtos(nome_produto, familia_produto, codigo_barras_produto)'
        'VALUES(?,?,?)', (self.nome_p, self.familia_p, self.codigo_b_p))

        Tabelaprodutos.conexao.commit()
    


    def alterar_nome(self):
        novonome = input("Digite aqui o novo nome do produto: ")
        id = input("Digite aqui o ID: ")
        Tabelaprodutos.cursor.execute(f'UPDATE produtos SET nome_produto = "{novonome}" WHERE id ="{id}"')
        Tabelaprodutos.conexao.commit()


    def alterar_familia(self):
        novafamilia = input("Digite aqui a nova familia do produto: ")
        id = input("Digite aqui o ID: ")
        Tabelaprodutos.cursor.execute(f'UPDATE produtos SET familia_produto ="{novafamilia}" WHERE id = "{id}"')
        Tabelaprodutos.conexao.commit()


    def alterar_codigo(self):
        codigo = input("Digite aqui o novo codigo do produto: ")
        Tabelaprodutos.cursor.execute(f'UPDATE produtos SET codigo_barras_produto ="{codigo}" WHERE id = "{id}"')
        Tabelaprodutos.conexao.commit()