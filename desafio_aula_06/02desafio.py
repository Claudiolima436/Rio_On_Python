# Uma empresa de vendas tem três corretores. A empresa paga ao corretor uma comissão calculada de acordo com o valor de suas vendas. Se o valor da venda de um corretor for maior que R$ 50.000.00 a comissão será de 12% do valor vendido. Se o valor da venda do corretor estiver entre R$ 30.000.00 e R$ 50.000.00 (incluindo extremos) a comissão será de 9.5%. Em qualquer outro caso, a comissão será de 7%. Escreva um programa que gere um relatório contendo nome, valor da venda e comissão de cada um dos corretores. O relatório deve mostrar também o total de vendas da empresa. 

#%%

# Listar corretores
corretores = []

# Solicitar informações sobre o corretor e sua venda
for i in range(3):
    nome = input(f"Digite o nome do corretor {i + 1}: ")
    valor_venda = float(input(f"Digite o valor da venda do corretor {nome}: R$ "))
    
# Calcular a comissão com base no valor da venda
    if valor_venda > 50000:
        comissao = valor_venda * 0.12
    elif 30000 <= valor_venda <= 50000:
        comissao = valor_venda * 0.095
    else:
        comissao = valor_venda * 0.07
    
    # Armazenar informaçõe
    corretores.append({
        "nome": nome,
        "valor_venda": valor_venda,
        "comissao": comissao
    })

# Calcular o total de vendas da empresa
total_vendas = sum(corretor["valor_venda"] for corretor in corretores)

# Gerar o relatório
print("\n--- Relatório de Vendas ---")
for corretor in corretores:
    print(f"Nome: {corretor['nome']}, Valor da Venda: R$ {corretor['valor_venda']:.2f}, Comissão: R$ {corretor['comissao']:.2f}")
print(f"\nTotal de vendas da empresa: R$ {total_vendas:.2f}")

# %%
