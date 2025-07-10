# Práctico 11: Aplicación de la Recursividad
# Ejercicio 2: Serie de Fibonacci recursiva

def fibonacci(n):
    """
    Función recursiva que calcula el valor de Fibonacci en la posición n
    """
    # Casos base: F(0) = 0 y F(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Caso recursivo: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Solicitar la posición hasta donde mostrar la serie
posicion = int(input("Ingrese hasta qué posición mostrar la serie de Fibonacci: "))

# Validar que la posición sea válida
if posicion < 0:
    print("Por favor ingrese un número no negativo.")
else:
    print(f"\n=== SERIE DE FIBONACCI HASTA LA POSICIÓN {posicion} ===")
    
    # Mostrar la serie completa desde la posición 0 hasta la posición indicada
    for i in range(posicion + 1):
        valor = fibonacci(i)
        print(f"F({i}) = {valor}")
    
    # Mostrar la serie en formato horizontal también
    print(f"\nSerie completa: ", end="")
    serie = []
    for i in range(posicion + 1):
        serie.append(str(fibonacci(i)))
    print(", ".join(serie))

# Para este ejercicio implementé la función recursiva de Fibonacci con sus casos base F(0)=0 y F(1)=1.
# El caso recursivo sigue la fórmula F(n) = F(n-1) + F(n-2).
# Muestro la serie tanto en formato vertical (con posiciones) como horizontal.
# Los recursos utilizados fueron: recursividad, casos base múltiples, bucles, listas y formateo de salida.
