'''
Cria agora um nove ficheiro python (extensão .py) com o nome ex04.
Escreve um programa que solicite duas notas ([nota1] e [nota2]) ao utilizador e apresente a média das mesmas da seguinte forma:
“A média das notas [nota1] e [nota2] é [média].”
'''

# Solicita as notas ao utilizador
nota1 = float(input("Introduza a primeira nota: "))
nota2 = float(input("Introduza a segunda nota: "))
# Calcula a média das notas
media = (nota1 + nota2) / 2
# Apresenta a média das notas
print(f"A média das notas {nota1} e {nota2} é {media}.")
      