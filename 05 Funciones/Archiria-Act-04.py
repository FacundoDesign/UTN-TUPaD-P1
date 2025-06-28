# EJERCICIO 4: Funciones para calcular área y perímetro de un círculo


# Importamos la biblioteca math para usar el valor de PI
import math

def calcular_area_circulo(radio):
    """
    Función que calcula el área de un círculo dado su radio.
    
    Fórmula: Área = π × radio²
    
    Parámetros:
        radio (float): Radio del círculo en unidades de longitud
    
    Retorna:
        float: Área del círculo en unidades cuadradas
    """
    # Aplicamos la fórmula del área: π × radio²
    # math.pi nos da el valor de π (3.14159...)
    # radio ** 2 significa radio elevado al cuadrado (radio × radio)
    area = math.pi * radio ** 2
    
    # Devolvemos el resultado calculado
    return area

def calcular_perimetro_circulo(radio):
    """
    Función que calcula el perímetro (circunferencia) de un círculo dado su radio.
    
    Fórmula: Perímetro = 2 × π × radio
    
    Parámetros:
        radio (float): Radio del círculo en unidades de longitud
    
    Retorna:
        float: Perímetro del círculo en unidades de longitud
    """
    # Aplicamos la fórmula del perímetro: 2 × π × radio
    # Multiplicamos 2 por pi por el radio
    perimetro = 2 * math.pi * radio
    
    # Devolvemos el resultado calculado
    return perimetro

# ====================================================================
# PROGRAMA PRINCIPAL
# ====================================================================

def main():
    """Función principal que ejecuta el programa."""
    
    # Mostramos el título del ejercicio
    print("="*60)
    print("EJERCICIO 4: Cálculos de Círculo (Área y Perímetro)")
    print("="*60)
    
    # Explicamos qué hace el programa
    print("Este programa calcula el área y perímetro de un círculo.")
    print("Solo necesitas proporcionar el radio del círculo.\n")
    
    # Mostramos las fórmulas que vamos a usar
    print(" Fórmulas utilizadas:")
    print("   • Área = π × radio²")
    print("   • Perímetro = 2 × π × radio")
    print(f"   • Valor de π = {math.pi:.6f}")
    print()
    
    # Solicitamos el radio al usuario
    print("Por favor, ingresa el radio del círculo:")
    
    try:
        # Convertimos el input a número decimal (float)
        radio_usuario = float(input("Radio: "))
        
        # Verificamos que el radio sea un valor positivo
        if radio_usuario <= 0:
            print("  El radio debe ser un número positivo.")
            print("Usando radio = 5 como ejemplo...")
            radio_usuario = 5
        
        # Mostramos los datos ingresados
        print(f"\n DATOS INGRESADOS:")
        print(f"   Radio del círculo: {radio_usuario}")
        
        # Llamamos a la primera función para calcular el área
        area_resultado = calcular_area_circulo(radio_usuario)
        
        # Llamamos a la segunda función para calcular el perímetro
        perimetro_resultado = calcular_perimetro_circulo(radio_usuario)
        
        # Mostramos los resultados de ambas funciones
        print(f"\n RESULTADOS CALCULADOS:")
        print(f"   Área del círculo: {area_resultado:.2f} unidades²")
        print(f"   Perímetro del círculo: {perimetro_resultado:.2f} unidades")
        
        # Mostramos cómo se realizaron los cálculos paso a paso
        print(f"\n🔍 DETALLE DE LOS CÁLCULOS:")
        print(f"   Área = π × {radio_usuario}² = {math.pi:.3f} × {radio_usuario**2} = {area_resultado:.2f}")
        print(f"   Perímetro = 2 × π × {radio_usuario} = 2 × {math.pi:.3f} × {radio_usuario} = {perimetro_resultado:.2f}")
        
    except ValueError:
        # Si el usuario no ingresa un número válido
        print(" Error: No ingresaste un número válido.")
        print("Vamos a usar un ejemplo con radio = 10")
        
        # Ejecutamos el ejemplo con radio = 10
        radio_ejemplo = 10
        area_ejemplo = calcular_area_circulo(radio_ejemplo)
        perimetro_ejemplo = calcular_perimetro_circulo(radio_ejemplo)
        
        print(f"\n📊 EJEMPLO CON RADIO = {radio_ejemplo}:")
        print(f"   Área: {area_ejemplo:.2f} unidades²")
        print(f"   Perímetro: {perimetro_ejemplo:.2f} unidades")
    
    # Ejemplos adicionales con diferentes valores
    print("\n" + "="*40)
    print("EJEMPLOS ADICIONALES:")
    print("="*40)
    
    # Lista de radios para mostrar ejemplos
    radios_ejemplo = [1, 2.5, 7, 15]
    
    # Mostramos la tabla de resultados
    print(f"{'Radio':<8} {'Área':<12} {'Perímetro':<12}")
    print("-" * 32)
    
    for radio in radios_ejemplo:
        area = calcular_area_circulo(radio)
        perimetro = calcular_perimetro_circulo(radio)
        print(f"{radio:<8} {area:<12.2f} {perimetro:<12.2f}")

# Ejecutamos el programa principal
if __name__ == "__main__":
    main()


# Detalle del codigo:
# Importamos 'math' para usar math.pi (valor de π)
# Creamos DOS funciones separadas: una para área y otra para perímetro
# Ambas funciones reciben el mismo parámetro (radio) pero hacen cálculos diferentes
# Las funciones DEVUELVEN los resultados calculados (no los imprimen)
# En el programa principal llamamos a AMBAS funciones con el mismo valor
# Guardamos los resultados en variables separadas y los mostramos
# Usamos float() para permitir números decimales en el radio
# Usamos :.2f para mostrar solo 2 decimales en los resultados
# Incluimos validación para asegurar que el radio sea positivo
