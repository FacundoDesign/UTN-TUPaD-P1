# EJERCICIO 7: Función que realiza operaciones básicas y devuelve tupla


def operaciones_basicas(a, b):
    """
    Función que recibe dos números y devuelve una tupla con las cuatro operaciones básicas.
    
    Parámetros:
        a (float): Primer número
        b (float): Segundo número
    
    Retorna:
        tuple: Tupla con (suma, resta, multiplicación, división)
               Si b=0, la división será un mensaje de error
    """
    # Calculamos cada operación por separado
    
    # 1. SUMA: a + b
    suma = a + b
    
    # 2. RESTA: a - b
    resta = a - b
    
    # 3. MULTIPLICACIÓN: a × b
    multiplicacion = a * b
    
    # 4. DIVISIÓN: a ÷ b (con validación para evitar división por cero)
    if b != 0:
        # Si b no es cero, realizamos la división normal
        division = a / b
    else:
        # Si b es cero, no podemos dividir, devolvemos un mensaje
        division = "Error: División por cero"
    
    # Creamos y devolvemos una tupla con los cuatro resultados
    # Una tupla se crea con paréntesis y elementos separados por comas
    resultados = (suma, resta, multiplicacion, division)
    
    return resultados

# ====================================================================
# PROGRAMA PRINCIPAL
# ====================================================================

def main():
    """Función principal que ejecuta el programa."""
    
    # Mostramos el título del ejercicio
    print("="*55)
    print("EJERCICIO 7: Operaciones Básicas (Devuelve Tupla)")
    print("="*55)
    
    # Explicamos qué hace el programa
    print(" Este programa realiza las cuatro operaciones básicas:")
    print("   • Suma (+)")
    print("   • Resta (-)")
    print("   • Multiplicación (×)")
    print("   • División (÷)")
    print(" Todas las operaciones se devuelven en una tupla.\n")
    
    # Solicitamos los dos números al usuario
    print("Ingresa dos números para realizar las operaciones:")
    
    try:
        # Pedimos el primer número
        print("Primer número (a):")
        numero_a = float(input("→ "))
        
        # Pedimos el segundo número
        print("Segundo número (b):")
        numero_b = float(input("→ "))
        
        # Mostramos los números ingresados
        print(f"\n NÚMEROS INGRESADOS:")
        print(f"   a = {numero_a}")
        print(f"   b = {numero_b}")
        
        # Llamamos a la función y recibimos la tupla de resultados
        # La función devuelve UNA tupla, pero podemos "desempaquetarla"
        resultados_tupla = operaciones_basicas(numero_a, numero_b)
        
        # Mostramos la tupla completa
        print(f"\n TUPLA DEVUELTA POR LA FUNCIÓN:")
        print(f"   {resultados_tupla}")
        
        # Desempaquetamos la tupla en variables individuales
        # Esto significa asignar cada elemento de la tupla a una variable
        suma, resta, multiplicacion, division = resultados_tupla
        
        # Mostramos cada resultado de forma clara
        print(f"\n RESULTADOS INDIVIDUALES:")
        print("-" * 35)
        print(f"Suma:           {numero_a} + {numero_b} = {suma}")
        print(f"Resta:          {numero_a} - {numero_b} = {resta}")
        print(f"Multiplicación: {numero_a} × {numero_b} = {multiplicacion}")
        
        # Para la división, verificamos si hay error
        if isinstance(division, str):
            # Si division es un string, es el mensaje de error
            print(f"División:       {numero_a} ÷ {numero_b} = {division}")
        else:
            # Si division es un número, mostramos el resultado
            print(f"División:       {numero_a} ÷ {numero_b} = {division:.4f}")
        
        # Mostramos diferentes formas de acceder a los elementos de la tupla
        print(f"\n🔍 ACCESO A ELEMENTOS DE LA TUPLA:")
        print(f"   resultados_tupla[0] (suma) = {resultados_tupla[0]}")
        print(f"   resultados_tupla[1] (resta) = {resultados_tupla[1]}")
        print(f"   resultados_tupla[2] (multiplicación) = {resultados_tupla[2]}")
        print(f"   resultados_tupla[3] (división) = {resultados_tupla[3]}")
        
    except ValueError:
        # Si el usuario no ingresa números válidos
        print(" Error: Debes ingresar números válidos.")
        print("Te mostraremos un ejemplo con números 15 y 3:\n")
        
        # Ejecutamos la función con números de ejemplo
        ejemplo_resultados = operaciones_basicas(15, 3)
        suma, resta, mult, div = ejemplo_resultados
        
        print(f" Tupla devuelta: {ejemplo_resultados}")
        print(f" Suma: 15 + 3 = {suma}")
        print(f" Resta: 15 - 3 = {resta}")
        print(f" Multiplicación: 15 × 3 = {mult}")
        print(f" División: 15 ÷ 3 = {div}")
    
    # Ejemplos adicionales
    print("\n" + "="*45)
    print("EJEMPLOS ADICIONALES:")
    print("="*45)
    
    # Lista de pares de números para ejemplos
    ejemplos = [
        (10, 2),
        (7, 0),    # Este mostrará el error de división por cero
        (25, 4),
        (-8, 3)
    ]
    
    # Procesamos cada ejemplo
    for a, b in ejemplos:
        resultado = operaciones_basicas(a, b)
        suma, resta, mult, div = resultado
        
        print(f"\n Ejemplo: operaciones_basicas({a}, {b})")
        print(f"   Tupla devuelta: {resultado}")
        print(f"   Suma: {suma}, Resta: {resta}, Multiplicación: {mult}, División: {div}")

# Función adicional para demostrar otros usos de tuplas
def comparar_operaciones(num1, num2, num3, num4):
    """
    Función que compara operaciones entre dos pares de números.
    
    Parámetros:
        num1, num2: Primer par de números
        num3, num4: Segundo par de números
    """
    print(f"\n COMPARACIÓN DE OPERACIONES:")
    print(f"   Primer par: {num1} y {num2}")
    print(f"   Segundo par: {num3} y {num4}")
    print("-" * 40)
    
    # Obtenemos las operaciones de ambos pares
    operaciones1 = operaciones_basicas(num1, num2)
    operaciones2 = operaciones_basicas(num3, num4)
    
    # Nombres de las operaciones
    nombres = ["Suma", "Resta", "Multiplicación", "División"]
    
    # Comparamos cada operación
    for i in range(4):
        print(f"{nombres[i]:13}: {operaciones1[i]:8} vs {operaciones2[i]:8}")

# Ejecutamos el programa principal
if __name__ == "__main__":
    main()
    
    # Ejemplo de función de comparación
    print("\n" + "="*50)
    print("FUNCIÓN EXTRA: COMPARACIÓN DE OPERACIONES")
    print("="*50)
    comparar_operaciones(12, 4, 20, 5)


# Detalle del Codigo:
# La función recibe DOS parámetros: a y b
# Calcula las cuatro operaciones básicas por separado
# Valida la división por cero antes de dividir
# DEVUELVE una tupla con los cuatro resultados: (suma, resta, mult, div)
# Una tupla es una estructura de datos INMUTABLE (no se puede cambiar)
# Se crea con paréntesis: (elemento1, elemento2, elemento3, elemento4)
# En el programa principal "desempaquetamos" la tupla en variables
# Podemos acceder a elementos individuales con índices: tupla[0], tupla[1], etc.
# La tupla permite devolver múltiples valores desde una función
# isinstance() verifica si una variable es de un tipo específico
