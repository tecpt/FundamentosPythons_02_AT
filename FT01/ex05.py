
import math 

#NOTAS

#############from math import sqrt - importar uma unica função

numero =math.sqrt(25)  # se importasse uma única função aqui a instrução mudaria para numero = sqrt(25)

#############################################


'''Sejam a e b os catetos de um triângulo retângulo, faz um programa que devolva o valor
da hipotenusa'''


a = float(input("Digite o valor do cateto a: "))
b = float(input("Digite o valor do cateto b: "))
hipotenusa = math.sqrt(a**2 + b**2)
print("A hipotenusa é: ", hipotenusa)




