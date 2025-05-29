# Actividad 9: Calcular media de números
# Elabora un programa que permita al usuario ingresar 100 números enteros 
# y luego calcule la media de esos valores.

print("=== ACTIVIDAD 9: CÁLCULO DE MEDIA ===")

# Cambiar esta variable a 100 para el programa final
# Se deja en 5 para facilitar las pruebas
CANTIDAD_NUMEROS = 5  # Cambiar a 100 para funcionamiento completo

print(f"Ingrese {CANTIDAD_NUMEROS} números enteros:")

suma_total = 0

# Solicitar y sumar todos los números
for i in range(CANTIDAD_NUMEROS):
    numero = int(input(f"Número {i + 1}: "))
    suma_total += numero

# Calcular la media
media = suma_total / CANTIDAD_NUMEROS

# Mostrar resultados
print(f"\n=== RESULTADOS ===")
print(f"Cantidad de números: {CANTIDAD_NUMEROS}")
print(f"Suma total: {suma_total}")
print(f"Media aritmética: {media:.2f}")

# Información adicional
if media == int(media):
    print(f"La media es un número entero: {int(media)}")
else:
    print(f"La media es un número decimal")
    print(f"Media redondeada: {round(media)}")
