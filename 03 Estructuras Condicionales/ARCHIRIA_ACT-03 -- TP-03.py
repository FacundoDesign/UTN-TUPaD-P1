#Práctico 3: Estructuras condicionales

#Actividad 3

# Programa que permite ingresar solo números pares
numero = int(input("Ingrese un número par: "))

if numero % 2 == 0:  # Si el resto de la división por 2 es cero, el número es par
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Para verificar si un número es par usé el operador % (módulo) que devuelve el resto de la división. Si un número dividido por 2 tiene resto 0, entonces es par.
