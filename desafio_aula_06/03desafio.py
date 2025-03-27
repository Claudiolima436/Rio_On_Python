# Um hotel cobra R$ 260.00 a diária de um casal e mais uma taxa de serviços. A taxa de serviços é de: • R$ 5.50 por diária, se o número de diárias for maior que 15; • R$ 6.00 por diária, se o número de diárias for igual a 15; • R$ 8.00 por diária, se o número de diárias for menor que 15. Construa um programa que mostre o nome e o total da conta de um cliente. 
#%%
# Solicitar nome do Hospede
#%%
# Entrada de informações de hospedes e numero de diarias
hospedes = input(" Informe o nome do hospede respónsavel: ")
diarias = int(input("Informe o número de diárias: "))
print (f"Nome do hospede: {hospedes} , Total de diarias: {diarias}")
#%%
# Valor da diária

valor_diaria = 260.00

# Calculo da taxa de serviço

if diarias > 15:
    taxa_servico = 5.50
elif diarias == 15:
    taxa_servico = 6.00
else:
    taxa_servico = 8.00

# Calculo do total da hospedagem, somado as devidas taxas

hospedagem = (valor_diaria + taxa_servico) * diarias
hospedagem


#%%
print(f"Nome do Hospede: {hospedes} , Valor da conta: {hospedagem:.2f}")





# %%
