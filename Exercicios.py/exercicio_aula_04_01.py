# Construa um programa onde o usuário irá fornecer o nome e o salário de um conjunto de funcionários. Ao final mostre o nome e o salário mais baixo e alto da empresa.


# Pede quantos funcionários serão cadastrados
#%%
quantidade = int(input("Quantos funcionários deseja cadastrar? "))
maior_salario = 0
nome_maior = ""

# Loop para cadastrar cada funcionário
for i in range(quantidade):
    nome = input(f"\nNome do {i+1}º funcionário: ")
    salario = float(input(f"Salário de {nome}: R$ "))
    
    # Verifica se é o maior salário até agora
    if salario > maior_salario:
        maior_salario = salario
        nome_maior = nome

# Mostra o resultado
print("\n--- Resultado ---")
print(f"Maior salário: {nome_maior} com R$ {maior_salario:.2f}")

#%%
# Construa um programa onde o usuário irá fornecer o nome e o salário de um conjunto de funcionários. Ao final mostre o nome e o salário mais baixo e mais alto da empresa.
 
# Entrada de Dados
sal_maior = 0
sal_menor = 100000
resp = "S"
 
# Processamento dos Dados - Inicio da Estrutura de Repetição
while resp == "S" or resp == "s":
    nome = input("Digite o Nome do Funcionario: ")
    salario = float(input("Digite o Salário do Funcionario: "))
    if salario > sal_maior:
        sal_maior = salario
        nome_maior = nome
    if salario < sal_menor:
        sal_menor = salario
        nome_menor = nome
    resp = input("Deseja Continuar? (S/N)")
# Processamento dos Dados - Fim da Estrutura de Repetição
 
# Saída de Dados
print(f"Sr(a) {nome_maior}, você possui o salário de R$ {sal_maior:.2f}, sendo o mais alto da empresa.")
print(f"Sr(a) {nome_menor}, você possui o salário de R$ {sal_menor:.2f}, sendo o mais abaixo da empresa.")

# %%
