#a. Devolva o preço do “prego”.
#b. Faça o print de todas as chaves do dicionário
#c. Acrescente na lista “omolete” com o preço de 5.
#d. Faça o print de todo o dicionário, para visualizar as alterações.
menu={
"entremeada": 7,
"Sardinha": 6,
"Filetes": 5.5,
"Prego": 7,
"Hamburguer": 5.5
}
print("a - Devolva o preço do “prego”.")
print("b - Faça o print de todas as chaves do dicionário")
print("c - Acrescente na lista “omolete” com o preço de 5.")
print("d - Faça o print de todo o dicionário, para visualizar as alterações.")
while True:
    user = input("Escolha uma opção:")
    match user:
        case "a":
            preço_prego = menu["Prego"]
            print(f"O preço do prego é {preço_prego}€")
        case "b":
            print(menu)
        case "c":
            menu.update({"Omolete": 5})
        case "d":
            print(menu)
        case _:
            print("Escolha uma opção entre a e d")