# Práctico 6: Estructuras de datos complejas
# Ejercicio 5: Análisis de palabras en una frase

print("=== EJERCICIO 5: ANÁLISIS DE PALABRAS EN UNA FRASE ===")

# Solicitar la frase al usuario
frase = input("Ingrese una frase: ").strip()

# Convertir la frase a minúsculas y dividir en palabras
palabras = frase.lower().split()

print(f"\nFrase ingresada: '{frase}'")
print(f"Total de palabras: {len(palabras)}")

# Crear un set con las palabras únicas
palabras_unicas = set(palabras)

print(f"\n=== PALABRAS ÚNICAS (usando set) ===")
print(f"Cantidad de palabras únicas: {len(palabras_unicas)}")
print("Palabras únicas:")
for palabra in sorted(palabras_unicas):  # Ordenadas alfabéticamente
    print(f"- {palabra}")

# Crear un diccionario con la cantidad de veces que aparece cada palabra
contador_palabras = {}

for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

print(f"\n=== CONTADOR DE PALABRAS (usando diccionario) ===")
print("Cantidad de apariciones de cada palabra:")
for palabra, cantidad in sorted(contador_palabras.items()):
    print(f"'{palabra}': {cantidad}")

# Mostrar estadísticas adicionales
print(f"\n=== ESTADÍSTICAS ADICIONALES ===")
palabra_mas_frecuente = max(contador_palabras, key=contador_palabras.get)
max_frecuencia = contador_palabras[palabra_mas_frecuente]
print(f"Palabra más frecuente: '{palabra_mas_frecuente}' ({max_frecuencia} veces)")

# Para este ejercicio utilicé el método .split() para dividir la frase en palabras.
# Convertí todo a minúsculas con .lower() para evitar duplicados por diferencias de mayúsculas.
# Los sets automáticamente eliminan duplicados, por lo que son perfectos para obtener palabras únicas.
# Para el contador, utilicé un diccionario donde incremento el valor si la clave existe, o la creo con valor 1.
# La función max() con key=contador_palabras.get me permite encontrar la palabra más frecuente.
# El método .items() me permite iterar sobre claves y valores del diccionario simultáneamente.
