# Escreva um programa que  dados os nomes e as duas notas de 5 alunoas, calcule a média e armazene-as em uma lista. Depois mostre os nomes, as notas e as médias dos alunos. Use a estrutura de repetição while.

#%%

nomes = []
medias = []


# Processamento dos dados - Inicio da estrutura de repetição
for i in range(5):
    nomes.append(input(f'Digite o nome do {i+1}o. aluno: '))
    n1 = float(input(f'Digite a primeira nota do {i+1}o. aluno: '))
    n2 = float(input(f'Digite a segunda nota do {i+1}o. aluno: '))
    medias.append((n1+n2)/2)
# Processamento dos dados - Fim da estrutura de repetição

print('\nLista com os Nomes e as Médias dos Alunos:')
# Saida de dados
for i in range(5):
    print(f'A média do Aluno {nomes[i]} foi: {medias[i]}')    


# %%
