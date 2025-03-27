# Faça um programa que receba do usuário o nome e a idade de 10 pessoas. Ao final mostre a média das idades e a idade da pessoa mais nova e mais velha.

soma = 0
idade = 0
idade_mais_nova = 0
idade_mais_velha = 0
nome_mais_nova = ""
nome_mais_velha = ""

for i in range(4):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    soma += idade
    if idade > idade_mais_velha:
        idade_mais_velha = idade
        nome_mais_velha = nome
    if idade < idade_mais_nova or idade_mais_nova == 0:
        idade_mais_nova = idade
        nome_mais_nova = nome

print(f"A média das idades é {soma / 4}")
print(f"A pessoa mais nova é {nome_mais_nova} com {idade_mais_nova} anos")
print(f"A pessoa mais velha é {nome_mais_velha} com {idade_mais_velha} anos")