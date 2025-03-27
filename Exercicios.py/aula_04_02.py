# Escreva um programa que, dado 5 números inteiros calcul a soma deles
#entrada de dados
soma = 0

# Processamento dos dados - Inicio da estrutura de repetição
for i in range(5):
    num = int(input("Digite um valor inteiro:"))
    soma = soma + num
# Processamento dos dados - Fim da estrutura de repetição

# Saída de dados
print(f"A soma dos valores digitados é: {soma}")
