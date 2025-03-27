#%%

# Calculadora Simples
# Objetivo: Criar uma calculadora de soma, subtração, multiplicação e divisão

# entrada de dados
num1 = float(input("Digite o primeiro número"))
num2 = float(input("Digite o segundo número"))


# entrada da operação
operacao = input("Digite a operação desejada (+, -, *, /) ")

# Operação e saida de dados
if operacao == "+":
    resultado = num1 + num2
    print(f"O resultado da soma é: {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == "/":
    if num2 != 0:  # Evitar divisão por zero
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Por favor, digite uma operação válida (+, -, *, /).")



# %%
