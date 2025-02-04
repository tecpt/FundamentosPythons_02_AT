'''Escreve um programa que solicite a temperatura em Fahrenheit (F), ao utilizador, e a converta para grau Celsius (C), devolvendo o resultado da conversão.
Use a fórmula: C = 5 * ((F-32) / 9).'''
# Solicita a temperatura em Fahrenheit
fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
# Calcula a temperatura em Celsius
celsius = 5 * ((fahrenheit - 32) / 9)
# Exibe o resultado da conversão
print(f"A temperatura de {fahrenheit}°F é igual a {celsius}°C")