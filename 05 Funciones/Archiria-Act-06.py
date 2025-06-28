# EJERCICIO 6: Función que muestra la tabla de multiplicar


def tabla_multiplicar(numero):
    """
    Función que imprime la tabla de multiplicar de un número del 1 al 10.
    
    Parámetros:
        numero (int): El número del cual queremos generar la tabla de multiplicar
    
    Esta función no retorna valores, solo imprime la tabla completa.
    """
    # Mostramos el encabezado de la tabla
    print(f"\n TABLA DE MULTIPLICAR DEL {numero}:")
    print("-" * 25)
    
    # Usamos un bucle for para generar las multiplicaciones del 1 al 10
    # range(1, 11) genera números del 1 al 10 (11 no incluido)
    for i in range(1, 11):
        # Calculamos el resultado de la multiplicación
        resultado = numero * i
        
        # Imprimimos la operación y su resultado con formato claro
        print(f"{numero} × {i:2} = {resultado:3}")
        # Explicación del formato:
        # - {numero} muestra el número base
        # - {i:2} muestra el multiplicador con 2 espacios de ancho
        # - {resultado:3} muestra el resultado con 3 espacios de ancho

# ====================================================================
# PROGRAMA PRINCIPAL
# ====================================================================

def main():
    """Función principal que ejecuta el programa."""
    
    # Mostramos el título del ejercicio
    print("="*50)
    print("EJERCICIO 6: Tabla de Multiplicar")
    print("="*50)
    
    # Explicamos qué hace el programa
    print(" Este programa genera la tabla de multiplicar de cualquier número.")
    print(" Mostrará las multiplicaciones del 1 al 10.\n")
    
    # Solicitamos el número al usuario
    print("Ingresa el número del cual quieres ver su tabla de multiplicar:")
    
    try:
        # Convertimos el input a número entero
        numero_usuario = int(input("Número: "))
        
        # Mostramos qué número eligió el usuario
        print(f"\n Has elegido el número: {numero_usuario}")
        
        # Llamamos a la función para generar y mostrar la tabla
        # Esta función no devuelve nada, solo imprime la tabla
        tabla_multiplicar(numero_usuario)
        
        # Mensaje de confirmación
        print(f"\n Tabla del {numero_usuario} generada exitosamente!")
        
    except ValueError:
        # Si el usuario no ingresa un número válido
        print(" Error: Debes ingresar un número entero.")
        print("Te mostraremos la tabla del 5 como ejemplo:\n")
        
        # Llamamos a la función con el número 5 como ejemplo
        tabla_multiplicar(5)
    
    # Preguntamos si quiere ver más tablas
    print("\n" + "="*35)
    print("¿QUIERES VER MÁS TABLAS?")
    print("="*35)
    
    # Bucle para permitir generar múltiples tablas
    while True:
        respuesta = input("\n¿Ver otra tabla? (s/n): ").lower().strip()
        
        if respuesta == 's' or respuesta == 'si' or respuesta == 'sí':
            # Si quiere ver otra tabla
            try:
                nuevo_numero = int(input("¿Qué número? "))
                tabla_multiplicar(nuevo_numero)
            except ValueError:
                print("Número no válido. Mostrando tabla del 3:")
                tabla_multiplicar(3)
        
        elif respuesta == 'n' or respuesta == 'no':
            # Si no quiere ver más tablas
            print("¡Gracias por usar el programa!")
            break
        
        else:
            # Si la respuesta no es clara
            print("Por favor responde 's' para sí o 'n' para no.")
    
    # Ejemplos de tablas comunes
    print("\n" + "="*40)
    print("EJEMPLOS DE TABLAS COMUNES:")
    print("="*40)
    
    # Lista de números para mostrar como ejemplo
    numeros_ejemplo = [2, 3, 7, 12]
    
    for numero in numeros_ejemplo:
        tabla_multiplicar(numero)
        print()  # Línea en blanco entre tablas

# Función adicional para mostrar comparación entre tablas
def comparar_tablas(num1, num2):
    """
    Función extra que muestra dos tablas lado a lado para comparar.
    
    Parámetros:
        num1 (int): Primer número
        num2 (int): Segundo número
    """
    print(f"\n COMPARACIÓN ENTRE TABLA DEL {num1} Y TABLA DEL {num2}:")
    print("-" * 55)
    print(f"{'TABLA DEL ' + str(num1):<25} {'TABLA DEL ' + str(num2):<25}")
    print("-" * 55)
    
    # Mostramos ambas tablas lado a lado
    for i in range(1, 11):
        resultado1 = num1 * i
        resultado2 = num2 * i
        print(f"{num1} × {i:2} = {resultado1:3}              {num2} × {i:2} = {resultado2:3}")

# Ejecutamos el programa principal
if __name__ == "__main__":
    main()
    
    # Ejemplo de comparación
    print("\n" + "="*50)
    print("FUNCIÓN EXTRA: COMPARACIÓN DE TABLAS")
    print("="*50)
    comparar_tablas(4, 6)

# Detalle del codigo:
# La función 'tabla_multiplicar' recibe un parámetro 'numero'
# Usamos un bucle for con range(1, 11) para iterar del 1 al 10
# En cada iteración calculamos: numero × i = resultado
# Usamos formato de cadenas para alinear la salida correctamente
# La función IMPRIME directamente (no devuelve valores)
# En el programa principal validamos que sea un número entero
# Agregamos un bucle while para permitir múltiples consultas
# Incluimos una función extra para comparar dos tablas
# Los dos puntos (:) en el formato controlan el ancho y alineación
# Esta función demuestra el uso de bucles dentro de funciones
