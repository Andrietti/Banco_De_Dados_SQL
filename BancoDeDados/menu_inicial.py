import sys
import time

sua_escolha = None
def menuinicial():
    print("""escolha:
[1] Opcao 1, Cadastrar um cliente
[2] Opcao 2, Editar o nome de um cliente
[3] Opcao 3, Editar o CPF de um cliente
[4] Opcao 4, Editar o CEP de um cliente
[5] Opcao 5, Cadastrar um produto
[6] Opcao 6, Editar o nome de um produto
[7] Opcao 7, Editar a familia de um produto
[8] Opcao 8, Editar o codigo de um produto
[9] Opcao 9, Cadastrar uma venda
[10] Opcao 10, Alterar o numero de quantidades
[11] Opcao 11, Alterar o valor unitario cadastrado"""
)



    

def escrever_bonitinho(texto):
    for letra in texto:
        print(letra, end="")
        time.sleep(0.06)


        
        