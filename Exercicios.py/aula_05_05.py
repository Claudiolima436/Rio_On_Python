#Construa um programa que armazene um conjunto de números inteiros em uma lista. Ao final mostrar a quantidade de elementos, a soma, a média, o maior e o menor valor.

# entrada de dados
#%%
numeros = []
resp = 's'

# Processamento dos dados - Inicio da estrutura de repetição
while resp == 's' or resp == 'S':
    numeros.append(int(input(f'Digite o {i}o. Valor: ')))
    i += 1
    resp = input('Deseja continuar? (s/n) ')
# Processamento dos dados - Fim da estrutura de repetição

# Saida de dados
print(f'Os números digitados foram: {numeros}')
print(f'Quantidade de elementos: {len(numeros)}')
print(f'Soma dos elementos: {sum(numeros)}')
print(f'Média dos elementos: {sum(numeros)/len(numeros)}')
print(f'Maior valor: {max(numeros)}')
print(f'Menor valor: {min(numeros)}')

# %%
