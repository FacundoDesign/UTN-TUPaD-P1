# EJERCICIO 8: Función para calcular el Índice de Masa Corporal (IMC)


def calcular_imc(peso, altura):
    """
    Función que calcula el Índice de Masa Corporal (IMC).
    
    Fórmula: IMC = peso (kg) ÷ altura² (m²)
    
    Parámetros:
        peso (float): Peso de la persona en kilogramos
        altura (float): Altura de la persona en metros
    
    Retorna:
        float: Valor del IMC calculado
    """
    # Aplicamos la fórmula del IMC
    # IMC = peso dividido por altura al cuadrado
    imc = peso / (altura ** 2)
    
    # Devolvemos el resultado calculado
    return imc

def interpretar_imc(imc):
    """
    Función adicional que interpreta el valor del IMC según los rangos estándar.
    
    Parámetros:
        imc (float): Valor del IMC calculado
    
    Retorna:
        str: Interpretación del IMC según rangos médicos
    """
    # Clasificamos el IMC según los rangos estándar de la OMS
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:  # imc >= 30
        return "Obesidad"

# ====================================================================
# PROGRAMA PRINCIPAL
# ====================================================================

def main():
    """Función principal que ejecuta el programa."""
    
    # Mostramos el título del ejercicio
    print("="*55)
    print("EJERCICIO 8: Calculadora de IMC")
    print("="*55)
    
    # Explicamos qué es el IMC y cómo se calcula
    print(" El IMC (Índice de Masa Corporal) es una medida que relaciona")
    print("   el peso y la altura para evaluar si una persona tiene un")
    print("   peso saludable.")
    print()
    print(" Fórmula: IMC = Peso (kg) ÷ Altura² (m²)")
    print()
    print(" Clasificación según la OMS:")
    print("   • Bajo peso:     IMC < 18.5")
    print("   • Peso normal:   18.5 ≤ IMC < 25")
    print("   • Sobrepeso:     25 ≤ IMC < 30")
    print("   • Obesidad:      IMC ≥ 30")
    print()
    
    # Solicitamos los datos al usuario
    print("Por favor, ingresa tus datos para calcular el IMC:")
    
    try:
        # Pedimos el peso en kilogramos
        print("Peso en kilogramos (ej: 70.5):")
        peso_usuario = float(input("→ "))
        
        # Validamos que el peso sea positivo
        if peso_usuario <= 0:
            print("  El peso debe ser un número positivo.")
            print("Usando 70 kg como ejemplo...")
            peso_usuario = 70
        
        # Pedimos la altura en metros
        print("Altura en metros (ej: 1.75):")
        altura_usuario = float(input("→ "))
        
        # Validamos que la altura sea positiva y realista
        if altura_usuario <= 0 or altura_usuario > 3:
            print("  La altura debe ser un número positivo menor a 3 metros.")
            print("Usando 1.70 m como ejemplo...")
            altura_usuario = 1.70
        
        # Mostramos los datos ingresados
        print(f"\n DATOS INGRESADOS:")
        print(f"   Peso: {peso_usuario} kg")
        print(f"   Altura: {altura_usuario} m")
        
        # Llamamos a la función para calcular el IMC
        imc_resultado = calcular_imc(peso_usuario, altura_usuario)
        
        # Mostramos el resultado con 2 decimales como solicita el ejercicio
        print(f"\n RESULTADO DEL CÁLCULO:")
        print(f"   Tu IMC es: {imc_resultado:.2f}")
        
        # Mostramos el cálculo paso a paso
        print(f"\n DETALLE DEL CÁLCULO:")
        print(f"   IMC = {peso_usuario} ÷ ({altura_usuario})²")
        print(f"   IMC = {peso_usuario} ÷ {altura_usuario ** 2:.4f}")
        print(f"   IMC = {imc_resultado:.2f}")
        
        # Usamos la función adicional para interpretar el resultado
        interpretacion = interpretar_imc(imc_resultado)
        
        print(f"\n INTERPRETACIÓN MÉDICA:")
        print(f"   Según tu IMC de {imc_resultado:.2f}, tienes: {interpretacion}")
        
        # Mostramos recomendaciones básicas según el resultado
        print(f"\n INFORMACIÓN ADICIONAL:")
        if imc_resultado < 18.5:
            print("   • Podrías considerar consultar con un profesional de la salud")
            print("   • Una dieta equilibrada puede ayudarte a ganar peso saludablemente")
        elif 18.5 <= imc_resultado < 25:
            print("   • ¡Felicitaciones! Tu peso está en el rango saludable")
            print("   • Mantén una dieta equilibrada y ejercicio regular")
        elif 25 <= imc_resultado < 30:
            print("   • Considera adoptar hábitos alimenticios más saludables")
            print("   • El ejercicio regular puede ayudarte a mantener un peso saludable")
        else:
            print("   • Es recomendable consultar con un profesional de la salud")
            print("   • Un plan de alimentación y ejercicio puede ser beneficioso")
        
    except ValueError:
        # Si el usuario no ingresa números válidos
        print(" Error: Debes ingresar números válidos.")
        print("Te mostraremos un ejemplo con peso 75 kg y altura 1.80 m:\n")
        
        # Ejecutamos la función con datos de ejemplo
        peso_ejemplo = 75
        altura_ejemplo = 1.80
        imc_ejemplo = calcular_imc(peso_ejemplo, altura_ejemplo)
        interpretacion_ejemplo = interpretar_imc(imc_ejemplo)
        
        print(f" Ejemplo: Peso = {peso_ejemplo} kg, Altura = {altura_ejemplo} m")
        print(f" IMC = {imc_ejemplo:.2f}")
        print(f" Clasificación: {interpretacion_ejemplo}")
    
    # Tabla de ejemplos con diferentes IMCs
    print("\n" + "="*60)
    print("TABLA DE EJEMPLOS CON DIFERENTES VALORES:")
    print("="*60)
    
    # Lista de ejemplos con diferentes pesos y alturas
    ejemplos = [
        (50, 1.60),   # Bajo peso
        (65, 1.70),   # Normal
        (80, 1.75),   # Sobrepeso
        (100, 1.70)   # Obesidad
    ]
    
    # Encabezado de la tabla
    print(f"{'Peso (kg)':<10} {'Altura (m)':<12} {'IMC':<8} {'Clasificación':<15}")
    print("-" * 50)
    
    # Procesamos cada ejemplo
    for peso, altura in ejemplos:
        imc = calcular_imc(peso, altura)
        clasificacion = interpretar_imc(imc)
        print(f"{peso:<10} {altura:<12} {imc:<8.2f} {clasificacion:<15}")

# Función adicional para calcular el peso ideal
def peso_ideal_rango(altura):
    """
    Función que calcula el rango de peso ideal para una altura dada.
    
    Parámetros:
        altura (float): Altura en metros
    
    Retorna:
        tuple: (peso_mínimo, peso_máximo) para IMC normal (18.5-24.9)
    """
    # Calculamos los pesos límite para IMC normal
    peso_min = 18.5 * (altura ** 2)  # IMC 18.5
    peso_max = 24.9 * (altura ** 2)  # IMC 24.9
    
    return (peso_min, peso_max)

# Ejecutamos el programa principal
if __name__ == "__main__":
    main()
    
    # Ejemplo de función adicional
    print("\n" + "="*50)
    print("FUNCIÓN EXTRA: RANGO DE PESO IDEAL")
    print("="*50)
    
    altura_ejemplo = 1.75
    peso_min, peso_max = peso_ideal_rango(altura_ejemplo)
    print(f"Para una altura de {altura_ejemplo} m:")
    print(f"Peso ideal: entre {peso_min:.1f} kg y {peso_max:.1f} kg")


# Detalle del Codigo:
# La función 'calcular_imc' recibe peso (kg) y altura (m)
# Aplica la fórmula: IMC = peso ÷ altura²
# Usa ** 2 para elevar la altura al cuadrado
# DEVUELVE el resultado como número decimal (float)
# Incluimos validaciones para valores positivos y realistas
# Mostramos el resultado con :.2f para 2 decimales como solicita
# Agregamos una función extra para interpretar el IMC
# Usamos rangos con if/elif/else para clasificar el resultado
# Incluimos información médica básica y recomendaciones
# La función adicional calcula rangos de peso saludable
