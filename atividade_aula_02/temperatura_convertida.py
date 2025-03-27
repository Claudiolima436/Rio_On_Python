#Faça um programa que leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A fórmula de conversão é: F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é a temperatura em Celsius.

# Solicitar a temperatura em graus Celsius
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Calcular a temperatura
fahrenheit = (9 * celsius + 160) / 5

# Saida de dados
print(f"A temperatura em graus Fahrenheit é: {fahrenheit:.2f}")
