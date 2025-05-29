# Actividad 5: Juego de adivinar número
# Crea un juego en el que el usuario deba adivinar un número aleatorio 
# entre 0 y 9. Al final, el programa debe mostrar cuántos intentos 
# fueron necesarios para acertar el número.

import random

print("=== ACTIVIDAD 5: JUEGO ADIVINAR NÚMERO ===")
print("¡Bienvenido al juego de adivinanza!")
print("Tienes que adivinar un número entre 0 y 9")

# Generar número aleatorio
numero_secreto = random.randint(0, 9)
intentos = 0

print("\n¡Comencemos!")

while True:
    try:
        intento = int(input("Ingresa tu número (0-9): "))
        
        if intento < 0 or intento > 9:
            print("Por favor, ingresa un número entre 0 y 9")
            continue
            
        intentos += 1
        
        if intento == numero_secreto:
            print(f"\n¡FELICITACIONES! 🎉")
            print(f"Adivinaste el número {numero_secreto}")
            print(f"Te tomó {intentos} intento{'s' if intentos != 1 else ''}")
            break
        elif intento < numero_secreto:
            print("El número secreto es MAYOR. Intenta de nuevo.")
        else:
            print("El número secreto es MENOR. Intenta de nuevo.")
            
    except ValueError:
        print("Por favor, ingresa un número válido")

print("\n¡Gracias por jugar!")
