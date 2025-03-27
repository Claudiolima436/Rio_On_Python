# Crie em python, um programa que simule um inventário de produtos.
# Cada produto deve ter nome,  preço e quantidade em estoque.
# Armazene os produtos em uma lista de dicionários.
# Calcule e imprima o valor total do inventário.

#%%

inventario = []  # cria o vetor lista inventário

# adicionar os produtos no vetor inventário
def adicionar_produto(nome, preco, quantidade):
    inventario.append({"nome" : nome, "preço" : preco, "quantidade" : quantidade})

def remover_produto(nome):
    for produto in inventario:
        if produto["nome"] == nome:
            inventario.remove(produto)
            return

adicionar_produto("mouse", 19.78, 10)
adicionar_produto("teclado", 37.78, 34)
adicionar_produto("monitor", 589.34, 43)
adicionar_produto("multifuncional", 435.25, 30)

print(inventario)
# %%
