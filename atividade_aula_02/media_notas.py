#Construa um programa onde o usuário irá fornecer as quatro notas de um aluno. Ao final apresente a média desse aluno. 

# Solicitar notas do aluno
Aluno = input("Insira o nome do aluno: ")
nota_01 = float(input("Digite a primeira nota: "))
nota_02 = float(input("Digite a segunda nota: "))
nota_03 = float(input("Digite a terceira nota: "))
nota_04 = float(input("Digite a quarta nota: "))

# Calcular a média das notas
media = (nota_01 + nota_02+ nota_03 + nota_04) / 4

# Saida de dados
print(f"O aluno {Aluno} obteve a média {media: .2f}")

