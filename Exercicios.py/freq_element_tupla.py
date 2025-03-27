#%%
# Contando a frequência de um elemento em uma lista

# Importando biblioteca Counter
from collections import Counter


# Definido uma lista
lista_nomes= ["Claudio", "Pedro", "Alessandra", "GUstavo", "Pedro", "Pedro", "Valkiria", "Stela", "Pedro"]

# Contando a frequencia de cada nome na lista
frequencia = Counter(lista_nomes)

# Encontrando o nome com mairo frequencia na lista
mais_frequente = frequencia.most_common(1)

# Saida de dados
print(f"O nome com maior frequencia é: {mais_frequente[0][0]}, com {mais_frequente[0][1]} aparições.")

