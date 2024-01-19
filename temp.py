import mysql.connector
from PyQt5 import uic, QtWidgets

config = {
    'user': 'root',
    'password': 'pedro12510',
    'host': '127.0.0.1',
    'port':'3306',
    'database': 'banco'
}

try:
    conn = mysql.connector.connect(**config)
    print("Conexão bem-sucedida!")

    # Criar um cursor para executar comandos SQL
    cursor = conn.cursor()
    def verifica_todos():
        cursor.execute("SELECT * FROM produtos;")
        dados = cursor.fetchall()
        print("( ID | Nome | Preço | Estoque )")
        for linha in dados:
            print(linha)
    def verifica_nome():
                    nome = str(input("Insira o nome do Produto: "))
                    print("( ID | Nome | Preço | Estoque )")
                    cursor.execute("SELECT * FROM produtos\n"
                                   f"Where NomeProduto = '{nome}';")
                    dados = cursor.fetchall()
                    for linha in dados:
                        print(linha)
    def verifica_preco_maior():
                    print("( ID | Nome | Preço | Estoque )")
                    cursor.execute("SELECT * FROM produtos ORDER BY PrecoProd DESC")
                    dados = cursor.fetchall()
                    for linha in dados:
                        print(linha)
    def verifica_preco_menor():
                    print("( ID | Nome | Preço | Estoque )")
                    cursor.execute("SELECT * FROM produtos ORDER BY PrecoProd ASC")
                    dados = cursor.fetchall()
                    for linha in dados:
                        print(linha)
    def ordena_maior():
                    print("( ID | Nome | Preço | Estoque )")
                    cursor.execute("SELECT * FROM produtos ORDER BY quantidade DESC")
                    dados = cursor.fetchall()
                    for linha in dados:
                        print(linha)
    def ordena_menor():
                    print("( ID | Nome | Preço | Estoque )")
                    cursor.execute("SELECT * FROM produtos ORDER BY quantidade ASC")
                    dados = cursor.fetchall()
                    for linha in dados:
                        print(linha)
    def adiciona_prod():
                nomeProd = str(input("Insira o nome do produto: "))
                precoProd = float(input("Insira agora qual será o preço do produto: "))
                quantidadeProd = int(input("Insira agora qual será a quantidade adicionada ao estoque: "))
                cursor.execute(f"INSERT INTO produtos (NomeProduto, PrecoProd, quantidade) VALUES ('{nomeProd}','{precoProd}','{quantidadeProd}');")
                conn.commit()
    def preco_prod(colunaTable):
        alteracao = str(input("Insira qual será o novo valor: "))
        cursor.execute(f"UPDATE produtos\n"
                        f"SET PrecoProd = '{alteracao}'\n"
                        f"WHERE NomeProduto = '{colunaTable}';")
        conn.commit()
    def adiciona_estoque(colunaTable):
        cursor.execute("SELECT quantidade FROM produtos\n"
                                       f"WHERE NomeProduto = '{colunaTable}'")
        dados = cursor.fetchone()
        for quantidadetotal in dados:
            print(f"Sua quantidade total é de {quantidadetotal} produtos em estoque\n")
        adicionar =  int(input("Insira a quantidade de produtos a serem inseridas no estoque: "))
        quantidadetotal += adicionar
        cursor.execute(f"UPDATE produtos\n"
                        f"SET quantidade = '{quantidadetotal}'\n"
                        f"WHERE NomeProduto = '{colunaTable}';")
        conn.commit()
    def remove_estoque(colunaTable):
        cursor.execute("SELECT quantidade FROM produtos\n"
                       f"WHERE NomeProduto = '{colunaTable}'")
        dados = cursor.fetchone()
        for quantidadetotal in dados:
            print(f"Sua quantidade total é de {quantidadetotal} produtos em estoque\n")
        subtrair =  int(input("Insira a quantidade de produtos a serem retirados do estoque: "))
        aux = quantidadetotal
        quantidadetotal -= subtrair
        if quantidadetotal < 0:
            print(f"O valor inserido não pode ser retirado pois existem apenas {aux} produtos no estoque.")
        else:
            cursor.execute(f"UPDATE produtos\n"
                f"SET quantidade = '{quantidadetotal}'\n"
                f"WHERE NomeProduto = '{colunaTable}';")
        conn.commit()
    def atualiza_preco():
                colunaTable = str(input("Insira o nome do Produto a ser alterado: "))
                digito = int(input('Insira um dos digitos a seguir\n'
                                   '1 - Para alterar o preço do produto\n'
                                   '2 - Para alterar a quantidade do produto no estoque\n'))
                if digito == 1:
                    preco_prod(colunaTable)
                elif digito == 2:
                    digito = int(input("Insira um dos digitos a seguir\n"
                                       "1 - para adicionar produtos ao estoque\n"
                                       "2 - para remover produtos do estoque\n"))
                    if digito == 1:
                        adiciona_estoque(colunaTable)
                    if digito == 2:
                        remove_estoque(colunaTable)
    def deleta_prod():
        condicaoDelete = str(input("Insira o nome do produto a ser removido do estoque: "))
        cursor.execute(f"DELETE FROM produtos\n"
                        f"WHERE NomeProduto = '{condicaoDelete}';")
    while True:
        digito = int(input('Digite os numeros a seguir para cada operação\n'
                        '1 - Para verificar produtos em estoque\n'
                        '2 - Para adicionar produto ao estoque\n'
                        '3 - Para atualizar o preço de um produto no estoque\n'
                        '4 - Para remover um produto do estoque\n'
                        '5 - Para fechar a conexão com o Sistema\n'))
        try:
            if digito == 1:
                int(input('Insira um dos digitos a seguir\n'
                    '1 - Para verificar todos os produtos\n'
                    '2 - Procurar produtos por nome\n'
                    '3 - Para Ordenar os produtos do maior para o menor preco\n'
                    '4 - Para Ordenar os produtos do menor para o maior preco\n'
                    '5 - Para Ordenar os produtos a partir da maior para a menor quantidade em estoque\n'
                    '6 - Para Ordenar os produtos a partir da menor para a maior quantidade em estoque\n'))
                if digito == 1:
                    verifica_todos()
                elif digito == 2:
                    verifica_nome()
                elif digito == 3:
                    verifica_preco_maior()
                elif digito == 4:
                    verifica_preco_menor()
                elif digito == 5:
                    ordena_maior()
                elif digito == 6:
                    ordena_menor()
                    
            elif digito == 2:
                adiciona_prod()
            elif digito == 3:
                atualiza_preco()
                
            elif digito == 4:
                deleta_prod()
                conn.commit()
            elif digito == 5:
                conn.commit()
                break
        except:
            print("Número digitado fora das opções.")
except mysql.connector.Error as err:
    print(f"Erro: {err}")

finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexão fechada.")
        
