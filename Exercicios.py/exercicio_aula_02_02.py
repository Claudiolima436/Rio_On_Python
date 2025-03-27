#Criar um programa onde o usuário irá fornecer dois valores inteiros: numerador e denominador. Ao final mostre o resultado e o resto da divisão.

#%%
numerador = int(input("Digite um valor inteiro: "))
denominador = int(input("Digite um valor inteiro"))


divisao = numerador / denominador
resto = numerador % denominador

# Exibir o resultado e o resto da divisão
print(f"Resultado da divisão de {numerador} por {denominador} é: {divisao}")
print(f"Resto da divisão: {resto}")


#%%

a = 5  # em binário: 0101
b = 3  # em binário: 0011

resultado = a ^ b  # em binário: 0110 (que é 6 em decimal)
print(resultado)  # Output: 6

# %%
