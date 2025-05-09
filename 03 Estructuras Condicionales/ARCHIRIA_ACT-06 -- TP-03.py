#Práctico 3: Estructuras condicionales

#Actividad 6


# Programa que analiza sesgo en una distribución
import random
from statistics import mode, median, mean

# Generar 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular la moda, mediana y media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

# Determinar el sesgo
if media > mediana > moda:
    print("La distribución tiene sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("La distribución tiene sesgo negativo (a la izquierda)")
else:
    print("La distribución no tiene sesgo")

#En esta actividad/ejercicio que es compleja, tuve que usar el paquete statistics y entender los conceptos de moda, mediana y media.
#Añadí prints para ver los valores calculados y poder verificar el resultado.
