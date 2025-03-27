#%%

# Classificação de Notas
# Objetivo: Classificar um aluno baseado na média final.

# Entrada de dados
Aluno = input("Digite o nome do aluno")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calculo da média
media = (nota1 + nota2 + nota3) / 3

# Classificar com base na média
if media >= 7:
    classificacao = "Aprovado"
elif 5 <= media < 7:
    classificacao = "Recuperação"
else:
    classificacao = "Reprovado"

# Saída de dados
print(f"Sua média é {media:.2f}. Status: {classificacao}.")

