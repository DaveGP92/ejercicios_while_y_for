# Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan, con un límite de tres peticiones.

password = input("Ingrese su contraseña: \n")
confirmation = input("Confirme su contraseña: \n")
intentos = 3

while password != confirmation:
    print("Las contraseñas no coinciden.")
    intentos -= 1
    print(f"Le quedan {intentos} intentos.")
    
    if intentos == 0:
        print("Cuenta bloqueada")
        break
    
    password = input("Ingrese de nuevo la contraseña:\n")
    confirmation = input("Confirme la contraseña:\n")

else:
    print("Las contraseñas coinciden.")
    
