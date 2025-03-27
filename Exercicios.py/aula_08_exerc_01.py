# %%
# Estrutura Simples e Declaração de Variáveis
# Exercício 1 - Saudação Personalizada
# Objetivo: Solicitar nome e idade do usuário e exibir uma mensagem.

nome = input("Digite seu nome?")
idade = int(input("Qual a sua idade?"))

if idade < 18:
    print(f"Olá {nome}, você ainda está iniciando sua jornada com {idade} anos!")
elif idade >=18:
    print(f"Olá {nome}, com {idade} anos, já deve ter alguma experiência!")




# %%
