# ====================================================================
# TRABAJO PRÁCTICO - FUNCIONES EN PYTHON
# EJERCICIO 3: Función que muestra información personal completa
# ====================================================================

def informacion_personal(nombre, apellido, edad, residencia):
    """
    Función que recibe cuatro parámetros e imprime información personal completa.
    
    Parámetros:
        nombre (str): Nombre de la persona
        apellido (str): Apellido de la persona
        edad (int): Edad de la persona en años
        residencia (str): Ciudad o lugar donde vive la persona
    
    Esta función no retorna valores, solo imprime la información formateada.
    """
    # Creamos el mensaje usando todos los parámetros recibidos
    # Usamos f-strings para formatear el mensaje de manera clara
    mensaje = f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"
    
    # Imprimimos el mensaje formateado
    print(mensaje)

# ====================================================================
# PROGRAMA PRINCIPAL
# ====================================================================

def main():
    """Función principal que ejecuta el programa."""
    
    # Mostramos el título del ejercicio
    print("="*50)
    print("EJERCICIO 3: Función Información Personal")
    print("="*50)
    
    # Explicamos al usuario qué vamos a hacer
    print("Te voy a pedir algunos datos personales para mostrar tu información completa.")
    print("Por favor, completa los siguientes campos:\n")
    
    # Solicitamos cada dato al usuario de forma individual y clara
    print("1. Nombre:")
    nombre_usuario = input("   → ")
    
    print("2. Apellido:")
    apellido_usuario = input("   → ")
    
    print("3. Edad:")
    # Para la edad, necesitamos convertir el input a número entero
    try:
        edad_usuario = int(input("   → "))
    except ValueError:
        # Si el usuario no ingresa un número válido, usamos un valor por defecto
        print("   ⚠️  No ingresaste un número válido. Usando 25 como edad por defecto.")
        edad_usuario = 25
    
    print("4. Ciudad/Lugar de residencia:")
    residencia_usuario = input("   → ")
    
    # Mostramos una línea separadora antes del resultado
    print("\n" + "-"*50)
    print("INFORMACIÓN PERSONAL PROCESADA:")
    print("-"*50)
    
    # Llamamos a la función con todos los datos recolectados
    # Esta función imprime directamente, no devuelve valores
    informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)
    
    # Ejemplo adicional con datos predefinidos
    print("\n" + "-"*30)
    print("EJEMPLO ADICIONAL:")
    print("-"*30)
    print("Llamando a la función con datos de ejemplo:")
    print("informacion_personal('Juan', 'Pérez', 28, 'Madrid')")
    print("Resultado:")
    
    # Llamamos a la función con datos de ejemplo para mostrar cómo funciona
    informacion_personal("Juan", "Pérez", 28, "Madrid")
    
    # Otro ejemplo
    print("\nOtro ejemplo:")
    print("informacion_personal('María', 'González', 22, 'Barcelona')")
    print("Resultado:")
    informacion_personal("María", "González", 22, "Barcelona")

# Ejecutamos el programa principal
if __name__ == "__main__":
    main()


# EXPLICACIÓN DEL CÓDIGO:

# La función recibe CUATRO parámetros: nombre, apellido, edad y residencia
# Todos los parámetros son obligatorios y deben pasarse en el orden correcto
# La función usa f-strings para crear un mensaje formateado con todos los datos
# Esta función IMPRIME directamente (no devuelve valores como la anterior)
# En el programa principal recolectamos cada dato por separado
# Para la edad usamos int() para convertir el texto a número
# Usamos try/except para manejar errores si el usuario no ingresa un número
# Al final llamamos a la función pasando los 4 argumentos en orden
