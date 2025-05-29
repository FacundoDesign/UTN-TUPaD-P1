# Actividad 6: Números pares en orden decreciente
# Desarrolla un programa que imprima en pantalla todos los números 
# pares comprendidos entre 0 y 100, en orden decreciente.

print("=== ACTIVIDAD 6: NÚMEROS PARES EN ORDEN DECRECIENTE ===")
print("Números pares del 100 al 0:")

contador = 0

for i in range(100, -1, -2):  # Desde 100 hasta 0, de 2 en 2
    print(i)
    contador += 1

print(f"\nSe imprimieron {contador} números pares en orden decreciente")
