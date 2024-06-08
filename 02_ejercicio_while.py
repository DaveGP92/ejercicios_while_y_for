# Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan, con un límite de tres peticiones.

contraseña = input("Ingrese su contraseña: \n")
confirmacion = input("Confirme su contraseña: \n")
intentos = 3

while contraseña != confirmacion:
    print("Las contraseñas no coinciden.")
    contraseña = input("Ingrese de nuevo la contraseña:\n")
    confirmacion = input("Confirme la contraseña:\n")

print("Las contraseñas coinciden.")
    
