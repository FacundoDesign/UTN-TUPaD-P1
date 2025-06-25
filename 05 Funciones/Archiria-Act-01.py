# ====================================================================
# TRABAJO PRÁCTICO - FUNCIONES EN PYTHON
# EJERCICIO 1: Función que imprime "Hola Mundo!"
# ====================================================================

def imprimir_hola_mundo():
    """
    Función que imprime el mensaje 'Hola Mundo!' por pantalla.
    
    Esta función no recibe parámetros y no devuelve valores.
    Su único propósito es mostrar un mensaje en la consola.
    """
    # Imprimimo el mensaje solicitado
    print("Hola Mundo!")

# ====================================================================
# PROGRAMA PRINCIPAL
# ====================================================================

def main():
    """Función principal que ejecuta el programa."""
    
    # Mostramos el título del ejercicio
    print("="*50)
    print("EJERCICIO 1: Función Hola Mundo")
    print("="*50)
    
    # Explicamos qué vamos a hacer
    print("Vamos a llamar a la función imprimir_hola_mundo()...")
    
    # Llamamos a la función desde el programa principal
    imprimir_hola_mundo()
    
    # Confirmamos que la función se ejecutó correctamente
    print("¡Función ejecutada exitosamente!")

# Ejecutamos el programa principal
if __name__ == "__main__":
    main()

# Detalles del Codigo:
# Defino una función llamada 'imprimir_hola_mundo' que no recibe parámetros
# Dentro de la función uso print() para mostrar el mensaje
# En el programa principal llamo a la función usando su nombre seguido de ()
# La función se ejecuta y muestra el mensaje por pantalla
