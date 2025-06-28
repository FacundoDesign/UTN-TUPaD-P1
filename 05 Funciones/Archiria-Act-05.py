# EJERCICIO 5: Función para convertir segundos a horas


def segundos_a_horas(segundos):
    """
    Función que convierte una cantidad de segundos a horas.
    
    Conversión: 1 hora = 3600 segundos
    Fórmula: horas = segundos ÷ 3600
    
    Parámetros:
        segundos (int): Cantidad de segundos a convertir
    
    Retorna:
        float: Cantidad de horas equivalente (puede tener decimales)
    """
    # Realizamos la conversión dividiendo entre 3600
    # 3600 segundos = 1 hora (60 minutos × 60 segundos)
    horas = segundos / 3600
    
    # Devolvemos el resultado de la conversión
    return horas

# ====================================================================
# PROGRAMA PRINCIPAL
# ====================================================================

def main():
    """Función principal que ejecuta el programa."""
    
    # Mostramos el título del ejercicio
    print("="*55)
    print("EJERCICIO 5: Conversión de Segundos a Horas")
    print("="*55)
    
    # Explicamos cómo funciona la conversión
    print(" Este programa convierte segundos a horas.")
    print(" Fórmula utilizada: Horas = Segundos ÷ 3600")
    print(" Recordatorio: 1 hora = 60 minutos = 3600 segundos\n")
    
    # Solicitamos la cantidad de segundos al usuario
    print("Por favor, ingresa la cantidad de segundos que deseas convertir:")
    
    try:
        # Convertimos el input a número entero
        segundos_usuario = int(input("Segundos: "))
        
        # Verificamos que sea un número positivo
        if segundos_usuario < 0:
            print("  Los segundos no pueden ser negativos.")
            print("Usando 7200 segundos como ejemplo...")
            segundos_usuario = 7200
        
        # Mostramos los datos ingresados
        print(f"\n DATOS INGRESADOS:")
        print(f"   Cantidad de segundos: {segundos_usuario}")
        
        # Llamamos a la función para realizar la conversión
        horas_resultado = segundos_a_horas(segundos_usuario)
        
        # Mostramos el resultado de la conversión
        print(f"\n RESULTADO DE LA CONVERSIÓN:")
        print(f"   {segundos_usuario} segundos = {horas_resultado:.4f} horas")
        
        # Mostramos el resultado de manera más comprensible
        if horas_resultado >= 1:
            # Si es 1 hora o más, mostramos horas completas y minutos restantes
            horas_completas = int(horas_resultado)  # Parte entera
            minutos_restantes = (horas_resultado - horas_completas) * 60  # Parte decimal × 60
            
            print(f"\n FORMATO MÁS COMPRENSIBLE:")
            if minutos_restantes > 0:
                print(f"   {segundos_usuario} segundos = {horas_completas} horas y {minutos_restantes:.1f} minutos")
            else:
                print(f"   {segundos_usuario} segundos = {horas_completas} horas exactas")
        else:
            # Si es menos de 1 hora, convertimos a minutos para mayor claridad
            minutos_totales = horas_resultado * 60
            print(f"\n FORMATO MÁS COMPRENSIBLE:")
            print(f"   {segundos_usuario} segundos = {minutos_totales:.1f} minutos")
        
        # Mostramos el cálculo paso a paso
        print(f"\n DETALLE DEL CÁLCULO:")
        print(f"   {segundos_usuario} ÷ 3600 = {horas_resultado:.4f} horas")
        
    except ValueError:
        # Si el usuario no ingresa un número válido
        print(" Error: Debes ingresar un número entero.")
        print("Vamos a usar ejemplos con diferentes valores...")
        
        # Ejecutamos ejemplos automáticamente
        ejemplos_segundos = [3600, 7200, 1800]
        
        for segundos in ejemplos_segundos:
            horas = segundos_a_horas(segundos)
            print(f"   {segundos} segundos = {horas:.2f} horas")
    
    # Tabla de conversiones comunes
    print("\n" + "="*45)
    print("TABLA DE CONVERSIONES COMUNES:")
    print("="*45)
    
    # Diccionario con conversiones típicas
    conversiones_comunes = {
        "1 minuto": 60,
        "5 minutos": 300,
        "15 minutos": 900,
        "30 minutos": 1800,
        "1 hora": 3600,
        "2 horas": 7200,
        "1 día": 86400,
        "1 semana": 604800
    }
    
    # Formato de tabla
    print(f"{'Tiempo':<12} {'Segundos':<10} {'Horas':<10}")
    print("-" * 32)
    
    # Mostramos cada conversión
    for descripcion, segundos in conversiones_comunes.items():
        horas = segundos_a_horas(segundos)
        print(f"{descripcion:<12} {segundos:<10} {horas:<10.2f}")
    
    # Ejemplo de uso práctico
    print(f"\n EJEMPLO PRÁCTICO:")
    print("   Si una película dura 9000 segundos:")
    horas_pelicula = segundos_a_horas(9000)
    print(f"   9000 segundos = {horas_pelicula:.2f} horas = {horas_pelicula * 60:.0f} minutos")

# Ejecutamos el programa principal
if __name__ == "__main__":
    main()

# Detalle del Codigo:
# La función recibe un parámetro 'segundos' (número entero)
# Realizamos la división: segundos ÷ 3600 para obtener las horas
# El resultado puede tener decimales (ej: 1.5 horas = 1 hora y 30 minutos)
# La función DEVUELVE el resultado como número decimal (float)
# En el programa principal convertimos el input a int() para segundos
# Llamamos a la función y guardamos el resultado
# Mostramos el resultado de diferentes formas para mayor comprensión
# Incluimos validación para números negativos
# Agregamos una tabla de conversiones comunes como referencia
# El formato :.4f muestra 4 decimales para mayor precisión
