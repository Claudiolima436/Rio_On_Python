# Escreva um programa que, dado 5 números inteiros calcul a soma deles
#%%
#entrada de dados
cont = 0
soma = 0

# Processamento dos dados - Inicio da estrutura de repetição
while cont < 5:
    num = int(input("Digite um valor inteiro:"))
    soma = soma + num
    cont += 1  # cont = cont + 1
# Processamento dos dados - Fim da estrutura de repetição

# Saída de dados
print(f"A soma dos valores digitados é: {soma}")

# %%
