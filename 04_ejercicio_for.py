print("Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.")

frase = input("Escriba una frase:\n").lower()

letra_escogida = input("Escoge una letra del alfabeto:\n").lower()

for letra in frase:
    if letra_escogida == letra:
        contador_letra = frase.count(letra_escogida)

print(f'La letra "{letra_escogida}" aparece {contador_letra} veces dentro de la frase o palabra "{frase}"')