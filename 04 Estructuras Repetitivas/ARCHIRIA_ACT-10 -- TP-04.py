# Actividad 10: Invertir dígitos de un número
# Escribe un programa que invierta el orden de los dígitos de un número 
# ingresado por el usuario. Ejemplo: si el usuario ingresa 547, 
# el programa debe mostrar 745.

print("=== ACTIVIDAD 10: INVERTIR DÍGITOS ===")

numero = int(input("Ingrese un número entero: "))

# Guardar el número original para mostrar
numero_original = numero

# Manejar el signo (números negativos)
es_negativo = numero < 0
numero_abs = abs(numero)

# Caso especial: si el número es 0
if numero_abs == 0:
    numero_invertido = 0
else:
    # Invertir los dígitos usando bucle while
    numero_invertido = 0
    temp = numero_abs
    
    while temp > 0:
        digito = temp % 10  # Obtener el último dígito
        numero_invertido = numero_invertido * 10 + digito  # Agregar al resultado
        temp //= 10  # Quitar el último dígito
    
    # Aplicar el signo original si era negativo
    if es_negativo:
        numero_invertido = -numero_invertido

# Mostrar resultado
print(f"\nResultado:")
print(f"Número original: {numero_original}")
print(f"Número invertido: {numero_invertido}")

# Verificación adicional mostrando el proceso
print(f"\nProceso de inversión:")
temp = abs(numero_original)
digitos = []
while temp > 0:
    digitos.append(temp % 10)
    temp //= 10

if digitos:
    print(f"Dígitos extraídos: {digitos}")
    print(f"Dígitos en orden original: {digitos[::-1]}")
    print(f"Dígitos en orden invertido: {digitos}")
