# Faça um programa que armazene em um vetor o nome e a idade de 10 pessoas. Ao final mostre o nome da pessoa mais velha.
#%%
nomes =[]
idades = []


for i in range(4):
    nomes.append(input(f'Digite o nome da {i+1}a. Pessoa: '))
    idades.append(int(input(f'Digite a idade da {i+1}a. Pessoa: ')))
    soma_idades = soma_idades + idades[i]

    print(f'A soma das idades das pessoas é {sum(idades)}')
    print(f'A média das idades das pessoas é {sum(idades)/len(idades)}')

# %%
print(f'A idade da pessoa mais velha é {max(idades)}')
print(f'A idade da pessoa mais nova é {min(idades)}')
# %%
print(f'A pessoa mais velha é {nomes[idades.index(max(idades))]}')
print(f'A pessoa mais nova é {nomes[idades.index(min(idades))]}')
# %%
print(f'A pessoa mais velha é {nomes[idades.index(max(idades))]} e tem {max(idades)} anos')
print(f'A pessoa mais nova é {nomes[idades.index(min(idades))]} e tem {min(idades)} anos')
# %%
