# Faça um programa que armazene em um vetor o nome, a média e a situação de um aluno de acordo com as condições abaixo. Ao final mostre o nome do aluno, seguido de sua média e sua situação. Mostre também a quantidade de alunos APROVADOS. - Se média < 30 REPROVADO; - Se média < 70 RECUPERAÇÃO;- Se média >= 70 APROVADO.

#%%


nomes = []
medias = []
situacoes = []


aprovados = 0


for i in range(5):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    media = float(input(f"Digite a média de {nome}: "))
    
   
    if media < 30:
        situacao = "REPROVADO"
    elif media < 70:
        situacao = "RECUPERAÇÃO"
    else:
        situacao = "APROVADO"
        aprovados += 1  
    
  
    nomes.append(nome)
    medias.append(media)
    situacoes.append(situacao)


print("\nResultados:")
for i in range(5):
    print(f"Aluno: {nomes[i]} | Média: {medias[i]:.2f} | Situação: {situacoes[i]}")


print(f"\nQuantidade de alunos APROVADOS: {aprovados}")

# %%
