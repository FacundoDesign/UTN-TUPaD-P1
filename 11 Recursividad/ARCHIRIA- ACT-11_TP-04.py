# Práctico 11: Aplicación de la Recursividad
# Ejercicio 4: Conversión de decimal a binario de forma recursiva

def decimal_a_binario(numero):
    """
    Función recursiva que convierte un número decimal a binario
    Retorna la representación binaria como cadena de texto
    """
    # Caso base: cuando el número es 0, retornamos "0"
    if numero == 0:
        return "0"
    # Caso base: cuando el número es 1, retornamos "1"
    elif numero == 1:
        return "1"
    # Caso recursivo: dividimos por 2 y concatenamos el resto
    else:
        # El resto de la división por 2 será 0 o 1
        resto = numero % 2
        # Llamada recursiva con el cociente de la división por 2
        return decimal_a_binario(numero // 2) + str(resto)

# Programa principal
print("=== CONVERSOR DECIMAL A BINARIO RECURSIVO ===")

# Solicitar número al usuario
numero = int(input("Ingrese un número entero positivo: "))

# Validar que el número sea positivo
if numero < 0:
    print("Por favor ingrese un número entero positivo.")
else:
    # Convertir a binario usando la función recursiva
    binario = decimal_a_binario(numero)
    
    # Mostrar el resultado
    print(f"\n=== RESULTADO ===")
    print(f"Número decimal: {numero}")
    print(f"Número binario: {binario}")
    
    # Mostrar el proceso paso a paso para entender mejor
    print(f"\n=== PROCESO DE CONVERSIÓN ===")
    temp = numero
    pasos = []
    
    while temp > 0:
        resto = temp % 2
        cociente = temp // 2
        pasos.append(f"{temp} ÷ 2 = {cociente} resto: {resto}")
        temp = cociente
    
    for paso in pasos:
        print(paso)
    
    print(f"Leyendo los restos de abajo hacia arriba: {binario}")
    
    # Verificar con algunos ejemplos adicionales
    print(f"\n=== EJEMPLOS ADICIONALES ===")
    ejemplos = [10, 15, 8, 1, 25]
    
    for num in ejemplos:
        bin_result = decimal_a_binario(num)
        print(f"{num} en binario: {bin_result}")

# Para este ejercicio implementé una función recursiva que sigue el algoritmo de división por 2.
# Los casos base son cuando el número es 0 o 1, y el caso recursivo divide por 2 y concatena el resto.
# También incluí una demostración paso a paso del proceso para mayor claridad.
# Los recursos utilizados fueron: recursividad, operadores módulo y división entera, concatenación de strings y bucles para ejemplos.
