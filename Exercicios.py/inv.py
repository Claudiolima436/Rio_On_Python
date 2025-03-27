#%%
# Programa para gerenciar um inventário de produtos

# Lista para armazenar os produtos (cada produto será um dicionário)
inventario = []

# Função para adicionar produtos ao inventário
def adicionar_produto(nome, preco, quantidade):
    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    inventario.append(produto)

# Função para calcular o valor total do inventário
def calcular_valor_total():
    total = sum(produto["preco"] * produto["quantidade"] for produto in inventario)
    return total

# Adicionando produtos ao inventário
adicionar_produto("Mouse", 19.78, 10)
adicionar_produto("Teclado", 39.90, 5)
adicionar_produto("Monitor", 450.00, 2)

# Calculando e exibindo o valor total do inventário
valor_total = calcular_valor_total()
print(f"Valor total do inventário: R$ {valor_total:.2f}")

# Exibindo os produtos do inventário
print("\nProdutos no inventário:")
for produto in inventario:
    print(f"{produto['nome']} - Preço: R$ {produto['preco']} - Quantidade: {produto['quantidade']}")

# %%
# Programa de Inventário de Produtos com Entrada do Usuário

# Lista para armazenar os produtos
inventario = []

# Função para adicionar produtos ao inventário
def adicionar_produto(nome, preco, quantidade):
    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    inventario.append(produto)

# Função para calcular o valor total do inventário
def calcular_valor_total():
    total = sum(produto["preco"] * produto["quantidade"] for produto in inventario)
    return total

# Entrada do usuário
print("Bem-vindo ao sistema de inventário!")
while True:
    nome = input("Digite o nome do produto (ou 'sair' para finalizar): ")
    if nome.lower() == "sair":
        break
    preco = float(input(f"Digite o preço do produto '{nome}': "))
    quantidade = int(input(f"Digite a quantidade em estoque do produto '{nome}': "))
    
    # Adiciona o produto ao inventário
    adicionar_produto(nome, preco, quantidade)

# Exibindo o inventário
print("\nProdutos cadastrados:")
for produto in inventario:
    print(f"{produto['nome']} - Preço: R$ {produto['preco']} - Quantidade: {produto['quantidade']}")

# Calculando e exibindo o valor total do inventário
valor_total = calcular_valor_total()
print(f"\nValor total do inventário: R$ {valor_total:.2f}")

# %%
