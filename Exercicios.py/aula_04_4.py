# Escreva um programa que, dado 5 numeros inteiros identifique o maior deles.
# Entrada de dados
maior = 0
# Processamento dos dados - Inicio da estrutura de repetição
	
for i in range(5):
    num = int(input("Digite um valor inteiro:"))
if num > maior:
	        maior = num
	# Processamento dos dados - fim da estrutura de repetição

	# Saida de dados
print (f"Maior número: {maior}")


