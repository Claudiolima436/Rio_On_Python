# Escreva um programa que leia três números inteiros e determine qual é o menor e qual é o maior.

#%%

numeros = []

for i in range(3):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
    
    
menor = min(numeros)
maior = max(numeros)

print(f"O menor número é {menor}")
print(f"O maior número é {maior}")

numeros

# %%
