
for i in range(1,11):
      print("5*%d=%d"%(i,5*i))
      
#ou

'''Escreve um programa que coloque no ecrã a tabuada do número 5.'''

print("\nTabuada do número 5:")
numero1 = 0
tabuada = 5
multiplicacao = 5
while numero1 <= 10:
    
    multiplicacao = tabuada * numero1 
    print(f"{tabuada} x {numero1} = {multiplicacao}")
    numero1 = numero1 + 1