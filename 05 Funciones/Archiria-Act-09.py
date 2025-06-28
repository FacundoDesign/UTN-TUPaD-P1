# Ejercicio 9: Conversor de temperatura Celsius a Fahrenheit

def celsius_a_fahrenheit(celsius):
    """
    Convierte temperatura de Celsius a Fahrenheit.
    
    Args:
        celsius (float): Temperatura en grados Celsius
    
    Returns:
        float: Temperatura en grados Fahrenheit
    """
    return (celsius * 9/5) + 32

# Programa principal para el ejercicio 9
print("--- EJERCICIO 9 ---")
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivale a {fahrenheit:.2f}°F")

# Para este ejercicio tuve que implementar la fórmula de conversión de Celsius a Fahrenheit.
# La fórmula es: F = (C × 9/5) + 32
# Usé la función celsius_a_fahrenheit() que recibe la temperatura en Celsius como parámetro
# y devuelve el resultado aplicando la fórmula matemática correspondiente.
# El resultado se muestra con 2 decimales usando :.2f en el formato de string.
