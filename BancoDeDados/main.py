import sqlite3
from tabela_clientes import Tabelacliente
from tabela_produtos import Tabelaprodutos
from tabela_vendas import Tabelavendas
from menu_inicial import *




dic = {1 : Tabelacliente.cadastrarcliente,
2: Tabelacliente.editar_nome_cliente,
3: Tabelacliente.editar_cpf_cliente,
4: Tabelacliente.editar_cep_cliente,
5: Tabelaprodutos.cadastrarproduto,
6: Tabelaprodutos.alterar_nome,
7: Tabelaprodutos.alterar_familia,
8: Tabelaprodutos.alterar_codigo,
9: Tabelavendas.cadastrarvenda,
10: Tabelavendas.alterar_quantidade,
11: Tabelavendas.alterar_valor_unitario
}

conexao = sqlite3.connect('exercicio.db')
cursor = conexao.cursor()
 

menuinicial()
opcao = int(input("Digite aqui sua escolha: "))

while True:
    if opcao not in range(1, 12):
        menuinicial()
        opcao = int(input("Selecione uma opcao valida: "))
    elif opcao ==  1:
        escrever_bonitinho("Digite o nome do cliente: ")
        nome_cliente = input()
        escrever_bonitinho("Porfavor, informe o cpf do cliente:")
        cpf_cliente = input()
        escrever_bonitinho("Okay, agora só falta o cep: ")
        cep_cliente = input()

        cliente = Tabelacliente(nome_cliente, cpf_cliente,cep_cliente)

        cliente.execute()
        
        
        dic[opcao](cliente)

    elif opcao < 5:
        try:
            dic[opcao](cliente)
        except NameError:
            print("Você ainda não cadastrou um cliente!")

    elif opcao == 5:
        escrever_bonitinho("Digite o nome do produto: ")
        nome_produto = input()
        escrever_bonitinho("Informe a familia do produto: ")
        familia_produto = input()
        escrever_bonitinho("Informe o codigo de barras do produto: ")
        cod_produto = input()

        produto = Tabelaprodutos(nome_produto, familia_produto, cod_produto)

        produto.execute()  

        dic[opcao](produto)

    elif opcao < 8:
        try:
            dic[opcao](produto)
        except NameError:
            print("Você ainda não cadastrou um produto")    




    elif opcao == 9:

        escrever_bonitinho("Digite aqui o codigo de barras do produto vendido: ")
        cod_produto_vendido = input()
        escrever_bonitinho("Digite aqui o cpf do comprador: ")
        cpf_comprador = int(input())
        escrever_bonitinho("Quantos produtos foram vendidos? ")
        quantidade_vendidos = float(input())
        escrever_bonitinho("Qual o valor unitário do produto? ")
        valor_unitario = float(input())

        venda = Tabelavendas(cod_produto_vendido, cpf_comprador, quantidade_vendidos, valor_unitario)

        venda.execute

        dic[opcao](venda)

    else:
        try:
            dic[opcao](venda)
        except NameError:
            print("Você ainda não cadastrou uma venda")

    
    print("""Você deseja continuar fazendo operações?
1 - Para sim
2 - Para nao""")
    escolha = int(input())
    if escolha == 1:
        menuinicial()
        opcao = int(input())
    else:
        print("Okay, até mais")
        break






    

cursor.close()
conexao.close()
