# Práctico 11: Aplicación de la Recursividad
# Ejercicio 5: Verificar si una palabra es palíndromo de forma recursiva

def es_palindromo(palabra):
    """
    Función recursiva que determina si una palabra es palíndromo
    No usa [::-1] ni reversed(), solo recursión
    """
    # Caso base: si la palabra tiene 0 o 1 caracteres, es palíndromo
    if len(palabra) <= 1:
        return True
    
    # Verificar si el primer y último carácter son iguales
    if palabra[0].lower() != palabra[-1].lower():
        return False
    
    # Caso recursivo: verificar la palabra sin el primer y último carácter
    return es_palindromo(palabra[1:-1])

# Programa principal
print("=== VERIFICADOR DE PALÍNDROMOS RECURSIVO ===")

# Solicitar palabra al usuario
palabra = input("Ingrese una palabra (sin espacios ni tildes): ").strip()

# Validar que no esté vacía
if not palabra:
    print("Por favor ingrese una palabra válida.")
else:
    # Verificar si es palíndromo
    resultado = es_palindromo(palabra)
    
    # Mostrar el resultado
    print(f"\n=== RESULTADO ===")
    print(f"Palabra: '{palabra}'")
    if resultado:
        print("✓ ES un palíndromo")
    else:
        print("✗ NO es un palíndromo")
    
    # Mostrar el proceso recursivo paso a paso
    print(f"\n=== ANÁLISIS PASO A PASO ===")
    def analizar_palindromo(palabra, nivel=0):
        """Función auxiliar para mostrar el proceso recursivo"""
        indentacion = "  " * nivel
        print(f"{indentacion}Analizando: '{palabra}'")
        
        if len(palabra) <= 1:
            print(f"{indentacion}→ Caso base: longitud ≤ 1, ES palíndromo")
            return True
        
        primer = palabra[0].lower()
        ultimo = palabra[-1].lower()
        print(f"{indentacion}→ Comparando '{primer}' con '{ultimo}'")
        
        if primer != ultimo:
            print(f"{indentacion}→ No coinciden, NO es palíndromo")
            return False
        
        print(f"{indentacion}→ Coinciden, analizar parte central: '{palabra[1:-1]}'")
        return analizar_palindromo(palabra[1:-1], nivel + 1)
    
    print("Proceso recursivo:")
    analizar_palindromo(palabra)
    
    # Probar con varios ejemplos
    print(f"\n=== EJEMPLOS ADICIONALES ===")
    ejemplos = ["oso", "casa", "radar", "nivel", "python", "reconocer", "a", ""]
    
    for ejemplo in ejemplos:
        if ejemplo:  # No procesar string vacío
            resultado_ejemplo = es_palindromo(ejemplo)
            estado = "✓ SÍ" if resultado_ejemplo else "✗ NO"
            print(f"'{ejemplo}' → {estado}")

# Para este ejercicio implementé una función recursiva que compara el primer y último carácter de la palabra.
# Los casos base son cuando la palabra tiene 0 o 1 caracteres (automáticamente palíndromo).
# El caso recursivo verifica si los extremos coinciden y luego analiza la parte central.
# También incluí una función auxiliar para mostrar el proceso paso a paso.
# Los recursos utilizados fueron: recursividad, slicing de strings, comparación de caracteres, y formateo de salida con indentación.
