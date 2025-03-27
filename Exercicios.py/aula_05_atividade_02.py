# Construa um programa que armazene o nome e o peso de um grupo de 5 pessoas em um vetor. Depois que a lista foi toda inserida o programa deve procurar e mostrar o peso médio do grupo e o nome da pessoa com mais peso e nome da pessoa com menos peso.

#%%
pessoas = ["Claudio", "Maria", "João", "Pedro", "Ana"]
pesos = [ 120, 70, 80, 90, 60]

peso_medio = sum(pesos) / len(pesos)
peso_max = max(pesos)
peso_min = min(pesos)

indice_peso_max = pesos.index(peso_max)
indice_peso_min = pesos.index(peso_min)

print(f'O peso médio do grupo é: {peso_medio:.2f} kg')
print(f'A pessoa mais pesada é {pessoas[indice_peso_max]} com {peso_max} kg')
print(f'A pessoa mais leve é {pessoas[indice_peso_min]} com {peso_min} kg')




# %%
