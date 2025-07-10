# Práctico 11: Aplicación de la Recursividad
# Ejercicio 3: Potencia recursiva usando la fórmula n^m = n * n^(m-1)

def potencia(base, exponente):
    """
    Función recursiva que calcula la potencia de un número
    usando la fórmula n^m = n * n^(m-1)
    """
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    # Caso recursivo: n^m = n * n^(m-1)
    else:
        return base * potencia(base, exponente - 1)

# Programa principal para probar la función
print("=== CALCULADORA DE POTENCIAS RECURSIVA ===")

# Solicitar base y exponente al usuario
base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente (número entero no negativo): "))

# Validar que el exponente sea no negativo
if exponente < 0:
    print("Este programa solo maneja exponentes no negativos.")
else:
    # Calcular la potencia usando la función recursiva
    resultado = potencia(base, exponente)
    
    # Mostrar el resultado
    print(f"\n=== RESULTADO ===")
    print(f"{base}^{exponente} = {resultado}")
    
    # Mostrar algunos ejemplos adicionales
    print(f"\n=== EJEMPLOS ADICIONALES ===")
    ejemplos = [(2, 3), (5, 2), (10, 0), (3, 4)]
    
    for b, e in ejemplos:
        res = potencia(b, e)
        print(f"{b}^{e} = {res}")

# Para este ejercicio implementé la función recursiva de potencia siguiendo la fórmula dada n^m = n * n^(m-1).
# El caso base es cuando el exponente es 0 (cualquier número elevado a 0 es 1).
# El caso recursivo multiplica la base por la potencia de la base elevada al exponente menos 1.
# Los recursos utilizados fueron: recursividad, validación de entrada, tuplas para ejemplos y formateo de salida.
