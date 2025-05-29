# Actividad 8: Análisis de 100 números
# Escribe un programa que permita al usuario ingresar 100 números enteros. 
# Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos.

print("=== ACTIVIDAD 8: ANÁLISIS DE NÚMEROS ===")

CANTIDAD_NUMEROS = 5 # Es posible cambiar facilmente este numero para probar con mas numeros = []

print(f"Ingrese {CANTIDAD_NUMEROS} números enteros:")

# Inicializar contadores
pares = 0
impares = 0
positivos = 0
negativos = 0
ceros = 0

# Procesar cada número
for i in range(CANTIDAD_NUMEROS):
    numero = int(input(f"Número {i + 1}: "))
    
    # Verificar par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    # Verificar signo
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1  # El cero no es positivo ni negativo

# Mostrar resultados
print(f"\n=== RESULTADOS DEL ANÁLISIS ===")
print(f"Total de números procesados: {CANTIDAD_NUMEROS}")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
if ceros > 0:
    print(f"Ceros: {ceros}")

# Verificaciones
print(f"\n=== VERIFICACIONES ===")
print(f"Pares + Impares = {pares + impares} (debe ser {CANTIDAD_NUMEROS})")
print(f"Positivos + Negativos + Ceros = {positivos + negativos + ceros} (debe ser {CANTIDAD_NUMEROS})")
