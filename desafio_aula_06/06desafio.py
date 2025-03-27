#  Foi feita uma pesquisa com um grupo de alunos de uma universidade, na qual se perguntou para cada aluno, o número de vezes que utilizou o restaurante da universidade no último mês. Construa um programa que determine:  
# a) O percentual de alunos que utilizaram menos que # 10 vezes o restaurante;  
# b) O percentual de alunos que utilizaram entre 10 e 15 vezes;  
# c) O percentual de alunos que utilizaram o restaurante acima de 15 vezes. 

#%%

# entrada de dados total de alunos
total_alunos = int(input("Digite o número total de alunos: "))

# determinando a quantidade

menos_de_10 = 0
entre_10_e_15 = 0
mais_de_15 = 0

# Verificando o numero de utilização
for i in range(total_alunos):
    vezes = int(input(f"Digite o número de vezes que o aluno {i + 1} utilizou o restaurante: "))
    
    if vezes < 10:
        menos_de_10 += 1
    elif 10 <= vezes <= 15:
        entre_10_e_15 += 1
    else:
        mais_de_15 += 1

# Calcular os percentuais
percentual_menos_de_10 = (menos_de_10 / total_alunos) * 100
percentual_entre_10_e_15 = (entre_10_e_15 / total_alunos) * 100
percentual_mais_de_15 = (mais_de_15 / total_alunos) * 100

# saida de dados
print("\n--- Resultado da Pesquisa ---")
print(f"Percentual de alunos que utilizaram menos de 10 vezes: {percentual_menos_de_10:.2f}%")
print(f"Percentual de alunos que utilizaram entre 10 e 15 vezes: {percentual_entre_10_e_15:.2f}%")
print(f"Percentual de alunos que utilizaram mais de 15 vezes: {percentual_mais_de_15:.2f}%")


