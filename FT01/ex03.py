'''um programa que receba, como parâmetro um inteiro, e
devolva o se dobro.
'''

numero = input("Introduza um valor inteiro:\n---->\t")
numero = int(numero)

dobro = 2*numero

output = "O dobro de %s é %s"%(numero,dobro)  #%s para string

output2 = "O dobro de {} é {}".format(numero,2*numero)

output3 = f"O dobro de {numero} é {dobro}" #formatted strings

print(f"O dobro de {numero} é {dobro}")  # Output: O dobro do