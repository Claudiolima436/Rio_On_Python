#  Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados de idade, sexo (M/F) e salário. Faça um programa que informe:  
# a) a média de salário do grupo;  
# b) a maior e a menor idade do grupo;  
# c) a quantidade de pessoas com salário acima de  R$ 5000,00. 

#%%

# Entrada de dados
num_habitantes = int(input("Digite o número de habitantes: "))

# listas dados
idades = []
sexos = []
salarios = []

# dados dos habitantes
for i in range(num_habitantes):
    print(f"\nHabitante {i + 1}:")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ").strip().upper()
    salario = float(input("Digite o salário: R$ "))
    
    idades.append(idade)
    sexos.append(sexo)
    salarios.append(salario)

# Calcular a média salarial
media_salarios = sum(salarios) / num_habitantes

# Encontrar a maior e a menor idade
maior_idade = max(idades)
menor_idade = min(idades)

#  pessoas com salário acima de R$ 5000,00
salarios_acima_5000 = sum(1 for salario in salarios if salario > 5000)

# Saida de dados
print("\n--- Relatório da Pesquisa ---")
print(f"Média de salário do grupo: R$ {media_salarios:.2f}")
print(f"Maior idade do grupo: {maior_idade} anos")
print(f"Menor idade do grupo: {menor_idade} anos")
print(f"Quantidade de pessoas com salário acima de R$ 5000,00: {salarios_acima_5000}")

# %%
