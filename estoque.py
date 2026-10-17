# ==============================================================
#   SISTEMA SIMPLES DE CONTROLE DE ESTOQUE
#   Linguagem: Python
#   Funcionalidade: Adicionar produtos e visualizar estoque
# ==============================================================

# ------------------------------
# 1. CRIAMOS UMA LISTA/CAIXA VAZIA PARA GUARDAR OS PRODUTOS
# Usamos um dicionário, que funciona como uma etiqueta: nome do produto = informações dele
# ------------------------------
estoque = {}


# ------------------------------
# 2. FUNÇÃO: ADICIONAR UM NOVO PRODUTO NO ESTOQUE
# 'def' significa "definir uma função" = um conjunto de comandos que podemos reutilizar
# ------------------------------
def adicionar_produto():
    # Pedimos ao usuário para digitar os dados do produto
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preço unitário: R$"))
    
    # Guardamos essas informações dentro do nosso dicionário 'estoque'
    estoque[nome] = {
        "quantidade": quantidade,
        "preco": preco
    }
    
    # Mensagem de confirmação
    print(f"✅ Produto '{nome}' cadastrado com sucesso!\n")


# ------------------------------
# 3. FUNÇÃO: MOSTRAR TODOS OS PRODUTOS CADASTRADOS
# ------------------------------
def mostrar_estoque():
    # Primeiro verificamos se o estoque está vazio
    if not estoque:
        print("📦 Estoque vazio! Cadastre algum produto primeiro.\n")
        return  # Sai da função sem fazer mais nada
    
    # Se tem produtos, mostramos tudo bonitinho
    print("=" * 50)
    print("📦            RELATÓRIO DE ESTOQUE")
    print("=" * 50)
    
    # Percorremos cada produto que está guardado no estoque
    for nome, dados in estoque.items():
        valor_total = dados["quantidade"] * dados["preco"]
        print(f"Produto:     {nome}")
        print(f"Quantidade:  {dados['quantidade']} unidades")
        print(f"Preço:       R$ {dados['preco']:.2f}")
        print(f"Total:       R$ {valor_total:.2f}")
        print("-" * 50)
    
    print()  # Linha em branco para organizar


# ------------------------------
# 4. MENU PRINCIPAL DO PROGRAMA
# 'while True' = repete o menu até o usuário escolher sair
# ------------------------------
while True:
    print("======= SISTEMA DE ESTOQUE =======")
    print("   1 - Adicionar produto")
    print("   2 - Ver todos os produtos")
    print("   3 - Sair do programa")
    print("=" * 35)
    
    opcao = input("Escolha uma opção (1, 2 ou 3): ")
    
    # Verificamos qual opção o usuário escolheu
    if opcao == "1":
        adicionar_produto()  # Chama a função de cadastrar
    elif opcao == "2":
        mostrar_estoque()    # Chama a função de mostrar
    elif opcao == "3":
        print("👋 Encerrando o sistema... Até logo!")
        break  # Encerra o loop e o programa acaba
    else:
        print("❌ Opção inválida! Digite apenas 1, 2 ou 3.\n")