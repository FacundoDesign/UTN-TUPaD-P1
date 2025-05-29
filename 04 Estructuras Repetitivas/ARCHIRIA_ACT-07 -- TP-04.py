# Actividad 7: Suma de números del 0 hasta un número dado
# Crea un programa que calcule la suma de todos los números 
# comprendidos entre 0 y un número entero positivo indicado por el usuario.

print("=== ACTIVIDAD 7: SUMA HASTA NÚMERO DADO ===")

while True:
    numero = int(input("Ingrese un número entero positivo: "))
    
    if numero < 0:
        print("Error: El número debe ser positivo. Intente nuevamente.")
        continue
    else:
        break

# Calcular la suma usando bucle for
suma = 0
for i in range(numero + 1):  # Del 0 al número inclusive
    suma += i

print(f"\nResultados:")
print(f"Suma de todos los números del 0 al {numero}: {suma}")

# Verificación usando la fórmula matemática n*(n+1)/2
suma_formula = numero * (numero + 1) // 2
print(f"Verificación con fórmula matemática: {suma_formula}")

if suma == suma_formula:
    print("✓ Cálculo correcto")
else:
    print("✗ Error en el cálculo")
