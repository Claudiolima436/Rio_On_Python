#Construa um programa que receba e armazene 10 números inteiros em um vetor. Ao final mostre o conteúdo do vetor e a soma deles.

#%%
numeros_inteiros = []

for i in range(10):
    numero = int(input('Digite um número inteiro: '))
    numeros_inteiros.append(numero)

print(f'Os números inteiros digitados foram: {numeros_inteiros}')
print(f'A soma dos números inteiros digitados é: {sum(numeros_inteiros)}')
