# Actividad 3: Suma entre dos valores
# Escribe un programa que sume todos los números enteros comprendidos 
# entre dos valores dados por el usuario, excluyendo esos dos valores.

print("=== ACTIVIDAD 3: SUMA ENTRE DOS VALORES ===")

# Solicitar los dos valores
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))

# Asegurar que valor1 sea menor que valor2
if valor1 > valor2:
    valor1, valor2 = valor2, valor1  # Intercambiar valores

# Sumar números entre los valores (excluyendo extremos)
suma = 0
contador = 0

for i in range(valor1 + 1, valor2):  # Excluye los extremos
    suma += i
    contador += 1

if contador > 0:
    print(f"La suma de los {contador} números entre {valor1} y {valor2} (excluyendo extremos) es: {suma}")
else:
    print(f"No hay números entre {valor1} y {valor2}")
