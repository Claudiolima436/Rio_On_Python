# Faça um programa para ler e armazenar em um vetor a temperatura média de uma determinada semana do mês. Calcular e escrever: 
# a) Menor temperatura do período;
# b) Maior temperatura do período
# c) Temperatura média período
# d) O número de dias do período em que a temperatura foi inferior a média

# %%
temperaturas = []
media = 0
menor = 0
maior = 0
inferior_media = 0

for i in range(7):
    temp = float(input(f"Digite a temperatura do dia {i+1}: "))
    temperaturas.append(temp)

menor = min(temperaturas)
maior = max(temperaturas)
media = sum(temperaturas) / len(temperaturas)
inferior_media = sum(1 for temp in temperaturas if temp < media)

print(f'Os números digitados foram: {temperaturas}')
print(f"Menor temperatura do período: {menor}")
print(f"Maior temperatura do período: {maior}")
print(f"Temperatura média do período: {media:.2f}")
print(f"Número de dias com temperatura inferior à média: {inferior_media}")


# %%
