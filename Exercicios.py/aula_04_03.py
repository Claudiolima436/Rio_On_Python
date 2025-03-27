# Escreva um programa que, dado conjunto de numeros inteiros, calcule a soma deles.
#entrada de dados
resp  = "S"
soma = 0

# Processamento dos dados - Inicio da estrutura de repetição
while resp == "S" or resp == "s":
    num = int(input("Digite um valor inteiro:"))
    soma = soma + num
    resp = input("Deseja continuar? (S/N)")
# Processamento dos dados - Fim da estrutura de repetição

# Saída de dados
print(f"A soma dos valores digitados é: {soma}")