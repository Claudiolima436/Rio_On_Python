# Faça um programa para ler 2 valores e se o segundo valor informado for zero, deve ser lido um novo valor, ou seja, para o segundo valor não pode ser aceito o valor zero e imprimir o resultado da divisão do primeiro valor pelo segundo valor.

valor_1 = float(input("Digite o primeiro valor: "))
valor_2 = float(input("Digite o segundo valor: "))
while valor_2 == 0:
    valor_2 = float(input("Digite um valor diferente de zero: "))

print(f"O resultado da divisão é {valor_1 / valor_2}")



