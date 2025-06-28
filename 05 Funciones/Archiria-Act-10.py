# ACTIVIDAD 10 - TP FUNCIONES

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

# Programa principal para el ejercicio 10
print("--- ACTIVIDAD 10 ---")
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")

# Para este ejercicio tuve que calcular el promedio aritmético de tres números.
# La fórmula del promedio es: (suma de todos los valores) / (cantidad de valores)
# Usé la función calcular_promedio() que recibe tres parámetros (a, b, c) y retorna
# la suma de los tres números dividida por 3.
# Los valores se solicitan al usuario como float para permitir números decimales
# y el resultado se muestra con 2 decimales usando :.2f en el formato de string.
