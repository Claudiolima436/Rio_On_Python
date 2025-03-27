# Faça um programa que calcule e mostre a tabuada de 0 a 10 de um número inteiro fornecido pelo usuário
# Entrada de dados
n = int(input("Digite um valor inteiro:"))
print(f"A Tabuada de {n} é:")
print("-------------------")
# Processamento dos dados - Inicio da estrutura de repetição
for i in range(11):
    print(f"{n} x {i} = {n*i}")
# Processamento dos dados - Fim da estrutura de repetição
