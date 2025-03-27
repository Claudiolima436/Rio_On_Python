#%%

# Criar uma função para calcular a média aritmética de 2 notas.

#nota1 = 9
#nota2 = 7
#media = (nota1 + nota2) / 2
#
#if media >= 7:
    #status = "Aprovado"
#elif media >= 5:
    #status = "Recuperação"
#else:
    #status = "Reprovado"
#print("Média", media)
#print("Situação", status)

#%%

def calcula_media(nota1,nota2):
    media = (nota1 + nota2)/2
    return media

#%%

def status_aluno(media):
    if media >=7:
        return "Aprovado"
    elif media < 5:
        return  "Reprovado"
    else:
        return  "Recuperação"


resultado = calcula_media(5,6)
print("Média", resultado)

sit = status_aluno(resultado)
print("Situação Aluno", sit)

    


# %%
