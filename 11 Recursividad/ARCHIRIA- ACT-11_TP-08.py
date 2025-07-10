# Práctico 11: Aplicación de la Recursividad
# Ejercicio 8: Contar cuántas veces aparece un dígito en un número

def contar_digito(numero, digito):
    """
    Función recursiva que cuenta cuántas veces aparece un dígito específico en un número
    """
    # Caso base: si el número es 0, no hay más dígitos que revisar
    if numero == 0:
        return 0
    
    # Obtener el último dígito del número
    ultimo_digito = numero % 10
    
    # Contar si el último dígito coincide con el dígito buscado
    coincidencia = 1 if ultimo_digito == digito else 0
    
    # Caso recursivo: coincidencia actual + contar en el resto del número
    return coincidencia + contar_digito(numero // 10, digito)

# Programa principal
print("=== CONTADOR DE DÍGITOS RECURSIVO ===")

# Solicitar datos al usuario
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese el dígito a buscar (0-9): "))

# Validar las entradas
if numero < 0:
    print("El número debe ser positivo.")
elif digito < 0 or digito > 9:
    print("El dígito debe estar entre 0 y 9.")
else:
    # Contar las apariciones del dígito
    apariciones = contar_digito(numero, digito)
    
    # Mostrar el resultado
    print(f"\n=== RESULTADO ===")
    print(f"Número: {numero}")
    print(f"Dígito buscado: {digito}")
    print(f"Apariciones: {apariciones}")
    
    # Mostrar el proceso recursivo paso a paso
    print(f"\n=== PROCESO RECURSIVO ===")
    def mostrar_proceso(num, dig, nivel=0):
        """Función auxiliar para mostrar el proceso recursivo"""
        indentacion = "  " * nivel
        print(f"{indentacion}contar_digito({num}, {dig})")
        
        if num == 0:
            print(f"{indentacion}→ Caso base: 0")
            return 0
        
        ultimo = num % 10
        resto = num // 10
        coincide = 1 if ultimo == dig else 0
        
        print(f"{indentacion}→ Último dígito: {ultimo}")
        print(f"{indentacion}→ Coincide con {dig}: {'SÍ' if coincide else 'NO'} ({coincide})")
        
        if resto > 0:
            print(f"{indentacion}→ Resto del número: {resto}")
            resultado_recursivo = mostrar_proceso(resto, dig, nivel + 1)
            resultado_total = coincide + resultado_recursivo
            print(f"{indentacion}→ {coincide} + {resultado_recursivo} = {resultado_total}")
            return resultado_total
        else:
            print(f"{indentacion}→ No hay más dígitos")
            return coincide
    
    print("Proceso paso a paso:")
    mostrar_proceso(numero, digito)
    
    # Verificar con los ejemplos del enunciado
    print(f"\n=== EJEMPLOS DEL ENUNCIADO ===")
    ejemplos = [
        (12233421, 2, 3),
        (5555, 5, 4),
        (123456, 7, 0)
    ]
    
    for num, dig, esperado in ejemplos:
        resultado = contar_digito(num, dig)
        print(f"contar_digito({num}, {dig}) = {resultado} (esperado: {esperado})")
        
        # Mostrar los dígitos del número para visualización
        digitos = []
        temp = num
        while temp > 0:
            digitos.append(temp % 10)
            temp //= 10
        digitos.reverse()
        print(f"  Dígitos de {num}: {digitos}")
        print(f"  Dígito {dig} aparece: {digitos.count(dig)} veces")
        print()
    
    # Ejemplos adicionales
    print(f"=== EJEMPLOS ADICIONALES ===")
    ejemplos_extra = [
        (1111, 1),
        (987654321, 5),
        (1000, 0),
        (999, 9)
    ]
    
    for num, dig in ejemplos_extra:
        resultado = contar_digito(num, dig)
        print(f"contar_digito({num}, {dig}) = {resultado}")

# Para este ejercicio implementé una función recursiva que examina cada dígito del número.
# El caso base es cuando el número llega a 0 (no hay más dígitos que examinar).
# El caso recursivo cuenta si el último dígito coincide con el buscado y continúa con el resto.
# Use operaciones matemáticas (% y //) para separar los dígitos sin convertir a string.
# Los recursos utilizados fueron: recursividad, operadores módulo y división entera, condicionales y visualización del proceso step-by-step.
