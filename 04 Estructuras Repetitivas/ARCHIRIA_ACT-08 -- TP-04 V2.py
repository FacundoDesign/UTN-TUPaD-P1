# Actividad 8: Análisis de números (versión mejorada)
# Escribe un programa que permita al usuario ingresar números enteros. 
# El usuario puede elegir cuántos números procesar (máximo 100).
# Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos.

print("=== ACTIVIDAD 8: ANÁLISIS DE NÚMEROS ===")

# Solicitar al usuario cuántos números desea procesar
while True:
    try:
        cantidad = int(input("¿Cuántos números desea procesar? (máximo 100): "))
        
        if cantidad <= 0:
            print("Error: Debe procesar al menos 1 número.")
        elif cantidad > 100:
            print("Error: No puede procesar más de 100 números.")
        else:
            break  # Cantidad válida
            
    except ValueError:
        print("Error: Ingrese un número entero válido.")

print(f"\nProcesando {cantidad} números...")
print("Ingrese los números enteros:")

# Inicializar contadores
pares = 0
impares = 0
positivos = 0
negativos = 0
ceros = 0

# Procesar cada número
for i in range(cantidad):
    while True:
        try:
            numero = int(input(f"Número {i + 1}: "))
            break
        except ValueError:
            print("Error: Ingrese un número entero válido.")
    
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
print(f"\n{'='*50}")
print(f"RESULTADOS DEL ANÁLISIS DE {cantidad} NÚMEROS")
print(f"{'='*50}")

print(f"Números pares: {pares} ({pares/cantidad*100:.1f}%)")
print(f"Números impares: {impares} ({impares/cantidad*100:.1f}%)")
print(f"Números positivos: {positivos} ({positivos/cantidad*100:.1f}%)")
print(f"Números negativos: {negativos} ({negativos/cantidad*100:.1f}%)")

if ceros > 0:
    print(f"Ceros: {ceros} ({ceros/cantidad*100:.1f}%)")

print(f"\n{'='*50}")
print("VERIFICACIONES:")
print(f"{'='*50}")
print(f"Pares + Impares = {pares + impares} (debe ser {cantidad}) ✓" if pares + impares == cantidad else f"Pares + Impares = {pares + impares} (debe ser {cantidad}) ✗")
print(f"Positivos + Negativos + Ceros = {positivos + negativos + ceros} (debe ser {cantidad}) ✓" if positivos + negativos + ceros == cantidad else f"Positivos + Negativos + Ceros = {positivos + negativos + ceros} (debe ser {cantidad}) ✗")

# Resumen estadístico adicional
print(f"\n{'='*50}")
print("RESUMEN ESTADÍSTICO:")
print(f"{'='*50}")

if pares > impares:
    print(f"• Hay más números pares ({pares}) que impares ({impares})")
elif impares > pares:
    print(f"• Hay más números impares ({impares}) que pares ({pares})")
else:
    print(f"• Hay la misma cantidad de números pares e impares ({pares})")

if positivos > negativos:
    print(f"• Hay más números positivos ({positivos}) que negativos ({negativos})")
elif negativos > positivos:
    print(f"• Hay más números negativos ({negativos}) que positivos ({positivos})")
else:
    print(f"• Hay la misma cantidad de números positivos y negativos ({positivos})")

print(f"\n¡Análisis completado exitosamente!")
