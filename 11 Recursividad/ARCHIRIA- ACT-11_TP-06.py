# Práctico 11: Aplicación de la Recursividad
# Ejercicio 6: Suma de dígitos de un número usando recursión

def suma_digitos(n):
    """
    Función recursiva que suma todos los dígitos de un número
    No convierte el número a string, usa solo operaciones matemáticas
    """
    # Caso base: si el número es menor que 10, tiene un solo dígito
    if n < 10:
        return n
    
    # Caso recursivo: último dígito + suma de los dígitos restantes
    ultimo_digito = n % 10  # Obtener el último dígito
    resto_numero = n // 10  # Obtener el número sin el último dígito
    
    return ultimo_digito + suma_digitos(resto_numero)

# Programa principal
print("=== CALCULADORA DE SUMA DE DÍGITOS RECURSIVA ===")

# Solicitar número al usuario
numero = int(input("Ingrese un número entero positivo: "))

# Validar que el número sea positivo
if numero < 0:
    print("Por favor ingrese un número entero positivo.")
else:
    # Calcular la suma de dígitos
    resultado = suma_digitos(numero)
    
    # Mostrar el resultado
    print(f"\n=== RESULTADO ===")
    print(f"Número: {numero}")
    print(f"Suma de dígitos: {resultado}")
    
    # Mostrar el proceso paso a paso
    print(f"\n=== PROCESO PASO A PASO ===")
    def mostrar_proceso(n, nivel=0):
        """Función auxiliar para mostrar el proceso recursivo"""
        indentacion = "  " * nivel
        print(f"{indentacion}suma_digitos({n})")
        
        if n < 10:
            print(f"{indentacion}→ Caso base: {n}")
            return n
        
        ultimo = n % 10
        resto = n // 10
        print(f"{indentacion}→ {n} % 10 = {ultimo} (último dígito)")
        print(f"{indentacion}→ {n} // 10 = {resto} (resto del número)")
        print(f"{indentacion}→ {ultimo} + suma_digitos({resto})")
        
        resultado_recursivo = mostrar_proceso(resto, nivel + 1)
        resultado_total = ultimo + resultado_recursivo
        print(f"{indentacion}→ {ultimo} + {resultado_recursivo} = {resultado_total}")
        
        return resultado_total
    
    print("Proceso recursivo:")
    mostrar_proceso(numero)
    
    # Probar con los ejemplos dados
    print(f"\n=== EJEMPLOS DEL ENUNCIADO ===")
    ejemplos = [1234, 9, 305]
    resultados_esperados = [10, 9, 8]
    
    for i, ejemplo in enumerate(ejemplos):
        resultado_ejemplo = suma_digitos(ejemplo)
        esperado = resultados_esperados[i]
        print(f"suma_digitos({ejemplo}) = {resultado_ejemplo} (esperado: {esperado})")
        
        # Mostrar la descomposición manual
        digitos = []
        temp = ejemplo
        while temp > 0:
            digitos.append(temp % 10)
            temp //= 10
        digitos.reverse()  # Para mostrar en orden normal
        suma_manual = sum(digitos)
        print(f"  Dígitos: {' + '.join(map(str, digitos))} = {suma_manual}")
        print()

# Para este ejercicio implementé una función recursiva que usa operaciones matemáticas exclusivamente.
# El caso base es cuando el número tiene un solo dígito (menor que 10).
# El caso recursivo separa el último dígito usando % 10 y el resto usando // 10.
# Incluí una función auxiliar que muestra todo el proceso de descomposición recursiva.
# Los recursos utilizados fueron: recursividad, operadores módulo y división entera, y formateo detallado del proceso.
