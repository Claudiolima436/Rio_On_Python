#Criar um programa onde o usuário forneça a descrição de um produto, o valor e a taxa de desconto. Ao final exibir o nome do produto e o valor com desconto.

# Entrada de dados
#%%
produto = input("Forneça a descrição do produto: ")
valor = float(input("Digite o valor do produto: "))
taxa_desconto = float(input("Digite  taxa de desconto: "))

# Calcular o valor do desconto
valor_desconto = valor * (taxa_desconto/100)

# Calcular o valor final com o desconto aplicado
valor_com_desconto = valor - valor_desconto

#%%

# Exibir o nome do produto e o valor com desconto

# %%

print(f"O produto {produto} com o desconto de {taxa_desconto} % tem o valor de R$ {valor_com_desconto:.2f}")
# %%
