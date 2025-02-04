'''Escreve um programa que calcule o volume de uma esfera. O valor do raio deverá ser
introduzido pelo utilizador'''
# Importar a biblioteca math para calcular a constante pi

import math
# Solicitar o valor do raio ao utilizador
raio = float(input("Introduza o valor do raio da esfera: "))
# Calcular o volume da esfera
volume = (4/3) * math.pi * (raio ** 3)
# Mostrar o resultado ao utilizador usando f-strings

print(f"O volume da esfera é {volume:.2f} cm³")

