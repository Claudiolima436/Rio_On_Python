#Crie um programa que calcule a idade de uma pessoa a partir do ano de nascimento dela.

#%%
from datetime import date

#%%
# Solicitar o ano de nascimento do usuário
ano_nascimento = int(input("Digite o ano de nascimento: "))

# Obter o ano atual
ano_atual = date.today().year

# Calcular a idade
idade = ano_atual - ano_nascimento

# Exibir a idade
print(f"A idade da pessoa é: {idade} anos")
# %%

#from datetime import date
#
## Solicitar a data de nascimento do usuário (dia, mês e ano)
#dia_nascimento = int(input("Digite o dia de nascimento: "))
#mes_nascimento = int(input("Digite o mês de nascimento: "))
#ano_nascimento = int(input("Digite o ano de nascimento: "))
#
## Obter a data atual
#data_atual = date.today()
#
## Calcular a idade
#idade = data_atual.year - ano_nascimento
#
## Verificar se o aniversário já passou no ano atual
#if (data_atual.month, data_atual.day) < (mes_nascimento, dia_nascimento):
    #idade -= 1
#
## Exibir a idade
#print(f"A idade da pessoa é: {idade} anos")

# %%
