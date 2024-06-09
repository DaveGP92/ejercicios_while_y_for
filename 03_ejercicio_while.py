import math
# Vamos a diseñar una calculadora que se enciende y hasta que no tecleamos 'SAL' no se apaga.

# Esta calculadora funciona de la siguiente manera:

# Recogemos los datos A y B
# Si operación es 1 calcula la raíz cuadrada de la suma de A y B
# Si operación es 2 calcula A / B. Vigilamos que B no sea 0...
# Si la operación es 3 calculamos la siguiente fórmula: ( A * B ) / 2.5

print("""    Bienvenido a mi calculadora. 
    Escoge una de las siguiente opciones para operar: """)

opcion = int(input("1: calcula la raíz cuadrada de la suma de A y B. '\n2: calcula A / B \n3: calculamos la siguiente fórmula: ( A * B ) / 2.5\n"))

while opcion not in [1,2,3]:
    opcion = int(input(f"{opcion} no es una opción válida. Escoge un número diferente\n"))

dict_opciones = {1 : "calcula la raíz cuadrada de la suma de A y B", 2 : "calcula A / B", 3 :"calculamos la siguiente fórmula: ( A * B ) / 2.5" }

print(f"Escogiste la opción {opcion}: {dict_opciones[opcion]}")


salida = input("Para salir escribe 'SAL', de lo contrario presiona cualquier tecla\n")

if salida != "SAL":
    print("Sigue la ejecución.")

    print("Ahora vamos a ingresar los números para operar: ")
    
    num1 = int(input("Ingresa el número A:\n"))

    while num1 == 0:
        num1 = int(input(f"{num1} no es una opción válida. Escoge un número diferente\n"))

    print(f"El número A es {num1}")

    num2 = int(input("Ingresa el número B:\n"))

    while num2 == 0:
        num2 = int(input(f"{num2} no es una opción válida. Escoge un número diferente\n"))

    while opcion == 0:
        print("Escoge un número diferente a 0")

    if opcion == 1:
        resultado = math.sqrt(num1 + num2)
        print(f"El resultado de a raíz cuadrada de la suma entre {num1} y {num2} es {resultado}")

    elif opcion == 2:
        resultado = num1 / num2
        print(f"El resultado de dividir {num1} entre {num2} es igual a {resultado}")
        
    else:
        resultado = (num1 * num2) / 2.5
        print(f"El resultado de multiplicar {num1} por {num2} y dividirlo entre 2.5 es igual a {resultado}")

else:
    print("Calculadora apagada")

