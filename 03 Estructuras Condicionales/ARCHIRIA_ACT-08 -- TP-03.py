#Práctico 3: Estructuras condicionales

#Actividad 8

# Programa que formatea un nombre según la opción elegida
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese una opción (1: mayúsculas, 2: minúsculas, 3: primera letra mayúscula): "))

if opcion == 1:
    nombre_formateado = nombre.upper()
elif opcion == 2:
    nombre_formateado = nombre.lower()
elif opcion == 3:
    nombre_formateado = nombre.title()
else:
    nombre_formateado = nombre  # Si no eligió una opción válida, dejamos el nombre como está
    print("Opción no válida. Se mostrará el nombre sin cambios.")

print(nombre_formateado)

#Usé los métodos upper(), lower() y title() para formatear el nombre según la opción elegida por el usuario.
