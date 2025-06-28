# EJERCICIO 2: Función que saluda con nombre personalizado
# 

def saludar_usuario(nombre):
    """
    Función que recibe un nombre como parámetro y devuelve un saludo personalizado.
    
    Parámetros:
        nombre (str): El nombre del usuario que queremos saludar
    
    Retorna:
        str: Un mensaje de saludo personalizado con el nombre
    """
    # Creamos el mensaje de saludo usando el parámetro nombre
    # Usamos f-strings para insertar el nombre en el mensaje
    mensaje_saludo = f"Hola {nombre}!"
    
    # Devolvemos el mensaje creado
    return mensaje_saludo

# ====================================================================
# PROGRAMA PRINCIPAL
# ====================================================================

def main():
    """Función principal que ejecuta el programa."""
    
    # Mostramos el título del ejercicio
    print("="*50)
    print("EJERCICIO 2: Función Saludo Personalizado")
    print("="*50)
    
    # Solicitamos el nombre al usuario
    print("Por favor, ingresa tu nombre para recibir un saludo personalizado.")
    nombre_usuario = input("Tu nombre: ")
    
    # Verificamos que el usuario haya ingresado algo
    if nombre_usuario.strip():  # strip() elimina espacios en blanco
        # Llamamos a la función saludar_usuario con el nombre ingresado
        # La función devuelve un valor, por lo que lo guardamos en una variable
        saludo_personalizado = saludar_usuario(nombre_usuario)
        
        # Mostramos el saludo devuelto por la función
        print(f"\nResultado de la función:")
        print(saludo_personalizado)
    else:
        # Si no ingresó nombre, mostramos un mensaje de error
        print("No ingresaste ningún nombre. Intentemos de nuevo.")
        print("Usando 'Usuario' como nombre por defecto...")
        
        # Llamamos a la función con un nombre por defecto
        saludo_defecto = saludar_usuario("Usuario")
        print(f"\nResultado de la función:")
        print(saludo_defecto)
    
    # Ejemplo adicional con diferentes nombres
    print("\n" + "-"*30)
    print("EJEMPLOS ADICIONALES:")
    print("-"*30)
    
    # Lista de nombres para mostrar más ejemplos
    nombres_ejemplo = ["María", "Carlos", "Ana", "Pedro"]
    
    # Iteramos sobre cada nombre y mostramos el saludo
    for nombre in nombres_ejemplo:
        saludo = saludar_usuario(nombre)
        print(f"saludar_usuario('{nombre}') → {saludo}")

# Ejecutamos el programa principal
if __name__ == "__main__":
    main()


# Detalles del codigo:
# La función 'saludar_usuario' recibe un parámetro llamado 'nombre'
# Dentro de la función creamos un mensaje usando f-strings para personalizar
# La función DEVUELVE el mensaje (no lo imprime directamente)
# En el programa principal pedimos el nombre al usuario con input()
# Llamamos a la función pasándole el nombre como argumento
# Guardamos el valor devuelto en una variable y lo mostramos
# La diferencia clave: esta función RETORNA un valor en lugar de solo imprimir
