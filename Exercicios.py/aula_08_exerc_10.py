#%%

# Soma de Números Ímpares até N
# Objetivo: Somar os números ímpares até um número N.

# Entrada de dados
N = int(input("Digite um número inteiro positivo: "))

# Soma dos ímpares
soma_impares = 0

# Usar um loop para somar os números ímpares
for i in range(1, N + 1): 
    if i % 2 != 0: 
        soma_impares += i 

# Saída de dados
print(f"A soma dos números ímpares até {N} é: {soma_impares}")


