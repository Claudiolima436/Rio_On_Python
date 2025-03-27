# Escreve um programa que armazene em uma lista os nomes de 5 pçessoas e depois mostre-os.

# %%

# entrada de dados
nome = []
for i in range(5):
    nome.append(input(f'Digite o nome da {i+1}a. Pessoa: '))

#%%
# Saida de dados
    print(f'Os nomes digitados foram: {nome}')
    for i in range(4):
        print(f'Nome da {i+1}a. Pessoa: {nome[i]}')


# %%

# entrada de dados
nome = []
resp = 's'

# Processamento dos dados - Inicio da estrutura de repetição
while resp == 's' or resp == 'S':
    nome.append(input(f'Digite o nome da {i+1}a. Pessoa: '))
    i += 1
    resp = input('Deseja continuar? (s/n) ')
# Processamento dos dados - Fim da estrutura de repetição

# Saida de dados
print(f'Os nomes digitados foram: {nome}')
for i in range(len(nome)):
    print(f'Nome da {i+1}a. Pessoa: {nome[i]}')
# %%
