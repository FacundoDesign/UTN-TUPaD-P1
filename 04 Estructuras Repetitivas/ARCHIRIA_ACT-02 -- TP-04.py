# Actividad 2: Contar dígitos de un número
# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

print("=== ACTIVIDAD 2: CONTAR DÍGITOS ===")

# Solicitar número al usuario
numero = int(input("Ingrese un número entero: "))

# Convertir a valor absoluto para manejar números negativos
numero_abs = abs(numero)

# Contar dígitos usando bucle while
if numero_abs == 0:
    digitos = 1  # El 0 tiene 1 dígito
else:
    digitos = 0
    temp = numero_abs
    while temp > 0:
        digitos += 1
        temp //= 10  # División entera

print(f"El número {numero} tiene {digitos} dígitos")
