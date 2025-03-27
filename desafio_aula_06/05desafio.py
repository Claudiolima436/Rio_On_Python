# Faça um programa que calcule a média de salários de uma empresa, pedindo ao usuário a quantidade de funcionários, o nome e o salário de cada funcionário e devolvendo a média, o salário mais alto e o salário mais baixo.

#%%
qtdefuncionarios = int(input("Digite o numero de funcionarios: "))

salarios = []
funcionarios = []

for i in range(qtdefuncionarios):
    nome = input(f"Digite o nome funcionario {i + 1}: ")
    salario = float(input(f"Digite o valor do salario do funcionario {nome}: R$ "))

    media_salarial = sum(salarios) / qtdefuncionarios

    funcionarios.append(nome)
    salarios.append(salario)

salario_mais_alto = max(salarios)
salario_mais_baixo = min(salarios)

print("\n---Relatório de salários---")
print(f"Média Salarial: R$ {media_salarial: .2f}")
print(f"Salário mais alto: R$ {salario_mais_alto:.2f}")
print(f"Salário mais baixo: R$ {salario_mais_baixo:.2f}")
# %%
