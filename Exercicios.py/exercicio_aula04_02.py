# Construa um programa onde o usuário irá fornecer o nome e o sexo de 10 pessoas. Ao final mostre a quantidade de pessoas do sexo masculino e do sexo feminino.
 
# Entrada de Dados
qtd_masc = 0
qtd_fem = 0
 
# Processamento dos Dados - Início da Estrutura de Repetição
for i in range(3):
    nome = input("Digite o Nome da Pessoa: ")
    sexo = input("Digite o Sexo da Pessoa (M ou F): ")
    if sexo == "M" or sexo == "m":
        qtd_masc += 1
    elif sexo == "F" or sexo == "f":
        qtd_fem += 1
    else:
        print("Sexo inválido")  
# Processamento dos Dados - Fim da Estrutura de Repetição
 
# Saída de Dados
print(f"Quantidade de pessoas do sexo masculino: {qtd_masc}")
print(f"Quantidade de pessoas do sexo feminino: {qtd_fem}")