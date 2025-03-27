# Construa um programa onde serão fornecidas as duas notas de dez alunos. Calcule a média de cada aluno e ao final mostre a média da turma.

nota_1 = 0
nota_2 = 0
media = 0
soma = 0

for i in range(5):
    nota_1 = float(input("Digite a primeira nota: "))
    nota_2 = float(input("Digite a segunda nota: "))
    media = (nota_1 + nota_2) / 2
    soma += media

print(f"A média da turma é {soma / 5}")



