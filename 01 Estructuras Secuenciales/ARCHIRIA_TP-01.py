#Actividad N1 - Estructuras Secuenciales

#Profesor: Sebastian Bruselario
#Alumno: Facundo Miguel Archiria

# Ejercicio 1: Crear un programa que imprima por pantalla el mensaje: "Hola Mundo!" 

print("Hola Mundo!") 

# Ejercicio 2: Crear un programa que pida al usuario su nombre e imprima un saludo 

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!") 

# Ejercicio 3: Pedir datos personales e imprimir una oración 

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ") 

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}") 

# Ejercicio 4: Calcular área y perímetro de un círculo
import math 

radio = float(input("Ingrese el radio del círculo: ")) 

area = math.pi * radio**2
perimetro = 2 * math.pi * radio 

print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}") 

# Ejercicio 5: Convertir segundos a horas 

segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600 

print(f"{segundos} segundos equivalen a {horas} horas") 

# Ejercicio 6: Mostrar tabla de multiplicar de un número 

numero = int(input("Ingrese un número: ")) 

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
print(f"{numero} x {i} = {numero * i}") 

# Ejercicio 7: Realizar operaciones aritméticas con dos números 

num1 = int(input("Ingrese el primer número (distinto de 0): "))
num2 = int(input("Ingrese el segundo número (distinto de 0): ")) 

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")


# Ejercicio 8: Calcular el índice de masa corporal (IMC) 

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: ")) 

imc = peso / (altura**2) 

print(f"Su índice de masa corporal es: {imc}") 

# Ejercicio 9: Convertir temperatura de Celsius a Fahrenheit 

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32 

print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit") 

# Ejercicio 10: Calcular el promedio de tres números 

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: ")) 

promedio = (num1 + num2 + num3) / 3 

print(f"El promedio de los tres números es: {promedio}")
