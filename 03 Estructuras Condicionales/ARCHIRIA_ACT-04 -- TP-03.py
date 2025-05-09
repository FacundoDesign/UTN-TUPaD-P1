#Práctico 3: Estructuras condicionales

#Actividad 4

# Programa que categoriza por edad
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:  # Si no es ninguna de las anteriores, es mayor o igual a 30
    print("Adulto/a")

#En este ejercicio usé múltiples condiciones (if-elif-else) para categorizar a la persona según su edad. Tuve que poner mucha atención a los límites para evitar errores.
