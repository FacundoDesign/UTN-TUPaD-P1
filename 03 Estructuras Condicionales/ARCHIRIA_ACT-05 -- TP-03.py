#Práctico 3: Estructuras condicionales

#Actividad 5

# Programa que valida la longitud de una contraseña
contraseña = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Usé la función len() para contar los caracteres de la contraseña y verifiqué que estuviera en el rango pedido.
