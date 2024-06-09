print("Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.")

palabra_selecc = input("Por favor, introduzca una palabra:\n")
palabra_reves = []

for letra in palabra_selecc:
    palabra_reves.append(letra)

palabra_reves.reverse()
print(palabra_reves)