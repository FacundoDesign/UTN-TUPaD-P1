# Práctico 11: Aplicación de la Recursividad
# Ejercicio 1: Factorial recursivo

def factorial(n):
    """
    Función recursiva que calcula el factorial de un número
    """
    # Caso base: el factorial de 0 y 1 es 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Solicitar el número al usuario
numero = int(input("Ingrese un número para calcular factoriales hasta ese valor: "))

# Validar que el número sea positivo
if numero < 1:
    print("Por favor ingrese un número entero positivo.")
else:
    print(f"\n=== FACTORIALES DESDE 1 HASTA {numero} ===")
    
    # Calcular y mostrar el factorial de todos los números desde 1 hasta el número ingresado
    for i in range(1, numero + 1):
        resultado = factorial(i)
        print(f"{i}! = {resultado}")

# Para este ejercicio implementé una función recursiva que calcula el factorial.
# La función tiene un caso base (cuando n es 0 o 1) y un caso recursivo donde n! = n * (n-1)!
# Luego uso un bucle for para mostrar todos los factoriales desde 1 hasta el número ingresado.
# Los recursos utilizados fueron: recursividad, validación de entrada, bucles y formateo de salida.
