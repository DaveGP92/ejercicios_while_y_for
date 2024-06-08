#Escriba un programa que pregunte una y otra vez si desea continuar el programa, salvo si se contesta exactamente no (en minúsculas).

respuesta = input("¿Desea continuar el programa?\n")

while respuesta != "no".lower():
    respuesta = input("¿Desea continuar el programa?\n")

print("Programa finalizado")