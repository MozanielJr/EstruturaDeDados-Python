import getpass
import os

def teste_login():
    usuario = input("Digite seu nome de usuário: ")
    senha = getpass.getpass("Digite sua senha: ")
    if usuario == 'diego' and senha == '123456'
    print("Acesso liberado")
    else:
    print("Acesso negado")

def listar_todos_produtos():
    if not os.path.isfile("produtos.txt"):
        print("A coleção está vazia.")
    else:
        with open("produtos.txt", "r") as arquivo_produto:
            produtos = arquivo_produto.read()
            if produtos:
                print("Lista de produtos:")
                print(produtos)
            else:
                print("A coleção está vazia.")


def salvar_produto(produtos):
    with open("produtos.txt", "w") as arquivo_produto:
        for produto in produtos:
            arquivo_produto.write(f"{produto}\n")


def listar_produto_por_id(produtos):
    if not produtos:
        print("A coleção de produtos está vazia.")
        return

    produto_id = int(input("Digite o ID do produto que deseja listar: "))
    encontrado = False
    for produto in produtos:
        if produto["id"] == produto_id:
            print(produto)
            encontrado = True
            break
    if not encontrado:
        print(f"Produto com ID {produto_id} não encontrado.")


def ordenar_produtos(produtos, ordem_da_funcao):
    if not produtos:
        print("A coleção está vazia.")
        return

    produtos_ordenados = sorted(produtos, key=lambda x: x["descricao"], reverse=ordem_da_funcao == "Z")
    print("Lista de produtos ordenados:")
    for produto in produtos_ordenados:
        print(produto)


def excluir_produto(produtos):
    if not produtos:
        print("A coleção de produtos está vazia.")
        return

    listar_todos_produtos()
    produto_id = int(input("Digite o ID do produto que deseja excluir: "))
    encontrado = False

    for produto in produtos:
        if produto["id"] == produto_id:
            produtos.remove(produto)
            print(f"Produto com ID {produto_id} excluído com sucesso!")
            encontrado = True
            break

    if not encontrado:
        print(f"Produto com ID {produto_id} não encontrado.")


def editar_produto(produtos):
    if not produtos:
        print("A coleção de produtos está vazia.")
        return

    listar_todos_produtos()
    produto_id = int(input("Digite o ID do produto que deseja editar: "))
    encontrado = False

    for produto in produtos:
        if produto["id"] == produto_id:
            print("Editar Produto:")
            produto["descricao"] = input(f"Nova descrição do produto ({produto['descricao']}): ")

            peso_input = input(f"Novo peso do produto ({produto['peso']} KG): ")
            peso_tokens = peso_input.split()

            if len(peso_tokens) == 2 and peso_tokens[1].upper() == "KG":
                try:
                    produto["peso"] = float(peso_tokens[0])
                except ValueError:
                    print("Peso inválido. Use um número válido seguido de 'KG'.")
            else:
                print("Formato de peso inválido. Use um número seguido de 'KG'.")

            produto['valor'] = float(input(f"Novo valor do produto ({produto['valor']}): "))
            produto['fornecedor'] = input(f"Novo fornecedor do produto ({produto['fornecedor']}): ")
            print(f"Produto com ID {produto_id} editado com sucesso!")
            encontrado = True
            break

    if not encontrado:
        print(f"Produto com ID {produto_id} não encontrado.")


def cadastrar_produto(produtos):
    produto = {}

    produto["id"] = len(produtos) + 1  # Autoincremento do ID
    produto["descricao"] = input("Digite a descrição do produto: ")

    peso_input = input("Digite o peso do produto (exemplo: 2.5 KG): ")
    peso_tokens = peso_input.split()

    if len(peso_tokens) == 2 and peso_tokens[1].upper() == "KG":
        try:
            produto["peso"] = float(peso_tokens[0])
        except ValueError:
            print("Peso inválido. Use um número válido seguido de 'KG'.")
            return
    else:
        print("Formato de peso inválido. Use um número seguido de 'KG'.")
        return

    produto["valor"] = float(input("Digite o valor do produto: "))
    produto["fornecedor"] = input("Digite o fornecedor do produto: ")
    produtos.append(produto)
    print("Produto cadastrado!")


# Carregar produtos a partir do arquivo, se existir.
produtos = []
if os.path.isfile("produtos.txt"):
    with open("produtos.txt", "r") as arquivo_produtos:
        produtos = eval(arquivo_produtos.read())

while True:
    teste_login()
    print("\n=== MENU ===")
    print("(1) Listar todos os produtos")
    print("(2) Listar produto pelo ID")
    print("(3) Listar todos os produtos ordenados (A/Z)")
    print("(4) Cadastrar novo produto")
    print("(5) Editar produto")
    print("(6) Excluir produto")
    print("(7) Sair do programa")

    opcao = input("Escolha a opção: ")

    if opcao == "1":
        listar_todos_produtos()
    elif opcao == "2":
        listar_produto_por_id(produtos)
    elif opcao == "3":
        ordem = input("Digite 'A' para ordem crescente ou 'Z' para ordem decrescente: ")
        ordenar_produtos(produtos, ordem)
    elif opcao == "4":
        cadastrar_produto(produtos)
        salvar_produto(produtos)
    elif opcao == "5":
        editar_produto(produtos)
        salvar_produto(produtos)
    elif opcao == "6":
        excluir_produto(produtos)
        salvar_produto(produtos)
    elif opcao == "7":
        print("Sair.")
        break
    else:
        print("Opção inválida.")
