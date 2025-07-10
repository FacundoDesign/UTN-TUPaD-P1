# Práctico 11: Aplicación de la Recursividad
# Ejercicio 7: Contar bloques de una pirámide de forma recursiva

def contar_bloques(n):
    """
    Función recursiva que cuenta el total de bloques necesarios para construir una pirámide
    donde el nivel más bajo tiene n bloques, el siguiente n-1, etc.
    """
    # Caso base: si solo hay 1 nivel, necesitamos 1 bloque
    if n == 1:
        return 1
    
    # Caso recursivo: bloques del nivel actual + bloques de los niveles superiores
    return n + contar_bloques(n - 1)

# Programa principal
print("=== CALCULADORA DE BLOQUES PARA PIRÁMIDE ===")

# Solicitar el número de bloques del nivel base
bloques_base = int(input("Ingrese el número de bloques en el nivel más bajo de la pirámide: "))

# Validar que sea un número positivo
if bloques_base < 1:
    print("El número de bloques debe ser mayor a 0.")
else:
    # Calcular el total de bloques necesarios
    total_bloques = contar_bloques(bloques_base)
    
    # Mostrar el resultado
    print(f"\n=== RESULTADO ===")
    print(f"Bloques en el nivel base: {bloques_base}")
    print(f"Total de bloques necesarios: {total_bloques}")
    
    # Mostrar la estructura de la pirámide
    print(f"\n=== ESTRUCTURA DE LA PIRÁMIDE ===")
    for nivel in range(bloques_base, 0, -1):
        espacios = " " * (bloques_base - nivel)
        bloques = "█ " * nivel
        print(f"Nivel {bloques_base - nivel + 1}: {espacios}{bloques}({nivel} bloques)")
    
    # Mostrar el proceso recursivo
    print(f"\n=== PROCESO RECURSIVO ===")
    def mostrar_calculo(n, nivel=0):
        """Función auxiliar para mostrar el cálculo recursivo"""
        indentacion = "  " * nivel
        print(f"{indentacion}contar_bloques({n})")
        
        if n == 1:
            print(f"{indentacion}→ Caso base: 1")
            return 1
        
        print(f"{indentacion}→ {n} + contar_bloques({n-1})")
        resultado_recursivo = mostrar_calculo(n - 1, nivel + 1)
        resultado_total = n + resultado_recursivo
        print(f"{indentacion}→ {n} + {resultado_recursivo} = {resultado_total}")
        
        return resultado_total
    
    print("Cálculo paso a paso:")
    mostrar_calculo(bloques_base)
    
    # Verificar con los ejemplos del enunciado
    print(f"\n=== EJEMPLOS DEL ENUNCIADO ===")
    ejemplos = [(1, 1), (2, 3), (4, 10)]
    
    for base, esperado in ejemplos:
        resultado = contar_bloques(base)
        print(f"contar_bloques({base}) = {resultado} (esperado: {esperado})")
        
        # Mostrar la suma manual
        suma_manual = sum(range(1, base + 1))
        niveles = " + ".join(str(i) for i in range(base, 0, -1))
        print(f"  Cálculo: {niveles} = {suma_manual}")
        print()
    
    # Mostrar algunos ejemplos adicionales
    print(f"=== EJEMPLOS ADICIONALES ===")
    for i in range(5, 8):
        resultado = contar_bloques(i)
        print(f"Pirámide de {i} niveles: {resultado} bloques")

# Para este ejercicio implementé una función recursiva que suma los bloques de cada nivel.
# El caso base es cuando hay solo 1 nivel (necesita 1 bloque).
# El caso recursivo suma los bloques del nivel actual más los bloques de todos los niveles superiores.
# Incluí una visualización de la pirámide y el proceso de cálculo recursivo.
# Los recursos utilizados fueron: recursividad, visualización con caracteres, formateo con espacios y cálculos de verificación.
