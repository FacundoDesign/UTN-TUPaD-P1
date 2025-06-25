import math

# ============================
# ACTIVIDAD 1
# ============================
def imprimir_hola_mundo():
    """Imprime el mensaje 'Hola Mundo!' por pantalla."""
    print("Hola Mundo!")

# ============================
# ACTIVIDAD 2
# ============================
def saludar_usuario(nombre):
    """
    Recibe un nombre como parámetro y devuelve un saludo personalizado.
    
    Args:
        nombre (str): El nombre del usuario
    
    Returns:
        str: Saludo personalizado
    """
    return f"Hola {nombre}!"

# ============================
# ACTIVIDAD 3
# ============================
def informacion_personal(nombre, apellido, edad, residencia):
    """
    Imprime información personal del usuario.
    
    Args:
        nombre (str): Nombre del usuario
        apellido (str): Apellido del usuario
        edad (int): Edad del usuario
        residencia (str): Lugar de residencia
    """
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# ============================
# ACTIVIDAD 4
# ============================
def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    
    Args:
        radio (float): Radio del círculo
    
    Returns:
        float: Área del círculo
    """
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    """
    Calcula el perímetro de un círculo dado su radio.
    
    Args:
        radio (float): Radio del círculo
    
    Returns:
        float: Perímetro del círculo
    """
    return 2 * math.pi * radio

# ============================
# ACTIVIDAD 5
# ============================
def segundos_a_horas(segundos):
    """
    Convierte segundos a horas.
    
    Args:
        segundos (int): Cantidad de segundos
    
    Returns:
        float: Cantidad de horas
    """
    return segundos / 3600

# ============================
# ACTIVIDAD 6
# ============================
def tabla_multiplicar(numero):
    """
    Imprime la tabla de multiplicar de un número del 1 al 10.
    
    Args:
        numero (int): Número para la tabla de multiplicar
    """
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# ============================
# ACTIVIDAD 7
# ============================
def operaciones_basicas(a, b):
    """
    Realiza operaciones básicas entre dos números.
    
    Args:
        a (float): Primer número
        b (float): Segundo número
    
    Returns:
        tuple: Tupla con (suma, resta, multiplicación, división)
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    
    return (suma, resta, multiplicacion, division)

# ============================
# ACTIVIDAD 8
# ============================
def calcular_imc(peso, altura):
    """
    Calcula el índice de masa corporal (IMC).
    
    Args:
        peso (float): Peso en kilogramos
        altura (float): Altura en metros
    
    Returns:
        float: IMC calculado
    """
    return peso / (altura ** 2)

# ============================
# ACTIVIDAD 9
# ============================
def celsius_a_fahrenheit(celsius):
    """
    Convierte temperatura de Celsius a Fahrenheit.
    
    Args:
        celsius (float): Temperatura en grados Celsius
    
    Returns:
        float: Temperatura en grados Fahrenheit
    """
    return (celsius * 9/5) + 32

# ============================
# ACTIVIDAD 10
# ============================
def calcular_promedio(a, b, c):
    """
    Calcula el promedio de tres números.
    
    Args:
        a (float): Primer número
        b (float): Segundo número
        c (float): Tercer número
    
    Returns:
        float: Promedio de los tres números
    """
    return (a + b + c) / 3

# ============================
# PROGRAMA PRINCIPAL
# ============================
def main():
    """Función principal que ejecuta todas las actividades."""
    
    print("="*50)
    print("TRABAJO PRÁCTICO - FUNCIONES EN PYTHON")
    print("="*50)
    
    # ACTIVIDAD 1
    print("\n--- ACTIVIDAD 1 ---")
    imprimir_hola_mundo()
    
    # ACTIVIDAD 2
    print("\n--- ACTIVIDAD 2 ---")
    nombre = input("Ingresa tu nombre: ")
    saludo = saludar_usuario(nombre)
    print(saludo)
    
    # ACTIVIDAD 3
    print("\n--- ACTIVIDAD 3 ---")
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = int(input("Ingresa tu edad: "))
    residencia = input("Ingresa tu lugar de residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)
    
    # ACTIVIDAD 4
    print("\n--- ACTIVIDAD 4 ---")
    radio = float(input("Ingresa el radio del círculo: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"Área del círculo: {area:.2f}")
    print(f"Perímetro del círculo: {perimetro:.2f}")
    
    # ACTIVIDAD 5
    print("\n--- ACTIVIDAD 5 ---")
    segundos = int(input("Ingresa la cantidad de segundos: "))
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos equivalen a {horas:.2f} horas")
    
    # ACTIVIDAD 6
    print("\n--- ACTIVIDAD 6 ---")
    numero = int(input("Ingresa un número para su tabla de multiplicar: "))
    tabla_multiplicar(numero)
    
    # ACTIVIDAD 7
    print("\n--- ACTIVIDAD 7 ---")
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    suma, resta, multiplicacion, division = operaciones_basicas(a, b)
    print(f"Suma: {a} + {b} = {suma}")
    print(f"Resta: {a} - {b} = {resta}")
    print(f"Multiplicación: {a} × {b} = {multiplicacion}")
    print(f"División: {a} ÷ {b} = {division}")
    
    # ACTIVIDAD 8
    print("\n--- ACTIVIDAD 8 ---")
    peso = float(input("Ingresa tu peso en kilogramos: "))
    altura = float(input("Ingresa tu altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Tu IMC es: {imc:.2f}")
    
    # ACTIVIDAD 9
    print("\n--- ACTIVIDAD 9 ---")
    celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius}°C equivale a {fahrenheit:.2f}°F")
    
    # ACTIVIDAD 10
    print("\n--- ACTIVIDAD 10 ---")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))
    promedio = calcular_promedio(num1, num2, num3)
    print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")
    
    print("\n" + "="*50)
    print("¡TRABAJO PRÁCTICO COMPLETADO!")
    print("="*50)

# Función para probar todas las funciones con valores de ejemplo
def pruebas_automaticas():
    """Ejecuta pruebas automáticas de todas las funciones."""
    
    print("\n" + "="*50)
    print("PRUEBAS AUTOMÁTICAS")
    print("="*50)
    
    # Prueba función 1
    print("\n1. Prueba imprimir_hola_mundo():")
    imprimir_hola_mundo()
    
    # Prueba función 2
    print("\n2. Prueba saludar_usuario('María'):")
    print(saludar_usuario("María"))
    
    # Prueba función 3
    print("\n3. Prueba informacion_personal('Juan', 'Pérez', 25, 'Buenos Aires'):")
    informacion_personal("Juan", "Pérez", 25, "Buenos Aires")
    
    # Prueba función 4
    print("\n4. Prueba cálculos de círculo (radio = 5):")
    area = calcular_area_circulo(5)
    perimetro = calcular_perimetro_circulo(5)
    print(f"Área: {area:.2f}")
    print(f"Perímetro: {perimetro:.2f}")
    
    # Prueba función 5
    print("\n5. Prueba segundos_a_horas(7200):")
    horas = segundos_a_horas(7200)
    print(f"7200 segundos = {horas} horas")
    
    # Prueba función 6
    print("\n6. Prueba tabla_multiplicar(3):")
    tabla_multiplicar(3)
    
    # Prueba función 7
    print("\n7. Prueba operaciones_basicas(10, 3):")
    resultados = operaciones_basicas(10, 3)
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicación: {resultados[2]}")
    print(f"División: {resultados[3]:.2f}")
    
    # Prueba función 8
    print("\n8. Prueba calcular_imc(70, 1.75):")
    imc = calcular_imc(70, 1.75)
    print(f"IMC: {imc:.2f}")
    
    # Prueba función 9
    print("\n9. Prueba celsius_a_fahrenheit(25):")
    fahrenheit = celsius_a_fahrenheit(25)
    print(f"25°C = {fahrenheit:.2f}°F")
    
    # Prueba función 10
    print("\n10. Prueba calcular_promedio(8, 9, 7):")
    promedio = calcular_promedio(8, 9, 7)
    print(f"Promedio: {promedio:.2f}")

# Ejecutar el programa
if __name__ == "__main__":
    # Puedes elegir ejecutar el programa principal interactivo o las pruebas automáticas
    
    opcion = input("¿Deseas ejecutar el programa interactivo (i) o las pruebas automáticas (p)? ").lower()
    
    if opcion == 'i':
        main()
    elif opcion == 'p':
        pruebas_automaticas()
    else:
        print("Ejecutando ambas opciones:")
        pruebas_automaticas()
        print("\n" + "="*50)
        print("AHORA EL PROGRAMA INTERACTIVO:")
        main()
