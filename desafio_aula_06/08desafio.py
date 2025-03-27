# Foi realizada uma pesquisa de algumas características físicas da população de uma certa região, a qual coletaram os seguintes dados referentes a cada habitante para serem analisados:  
# - sexo (masculino e feminino)  
# - cor dos olhos (azuis, verdes ou castanhos)  
# - cor dos cabelos (louros, castanhos, pretos)  
# - idade  
# Faça um programa que determine e escreva:  
# a) a maior idade dos habitantes;  
# b) a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive;  
# c) a quantidade de indivíduos que tenham olhos verdes e cabelos louros

#%%

num_habitantes = int(input("Digite o número de habitantes: "))

maior_idade = 0
feminino_18_35 = 0
olhos_verdes_cabelos_louros = 0

for i in range(num_habitantes):
    print(f"\nHabitante {i + 1}:")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ").strip().upper()
    cor_olhos = input("Digite a cor dos olhos (azuis, verdes, castanhos): ").strip().lower()
    cor_cabelos = input("Digite a cor dos cabelos (louros, castanhos, pretos): ").strip().lower()
    
    
    maior_idade = max(maior_idade, idade)
    
   
    if sexo == "F" and 18 <= idade <= 35:
        feminino_18_35 += 1
    
   
    if cor_olhos == "verdes" and cor_cabelos == "louros":
        olhos_verdes_cabelos_louros += 1


print("\n--- Resultados da Pesquisa ---")
print(f"a) Maior idade dos habitantes: {maior_idade} anos")
print(f"b) Quantidade de mulheres com idade entre 18 e 35 anos: {feminino_18_35}")
print(f"c) Quantidade de pessoas com olhos verdes e cabelos louros: {olhos_verdes_cabelos_louros}")

# %%
