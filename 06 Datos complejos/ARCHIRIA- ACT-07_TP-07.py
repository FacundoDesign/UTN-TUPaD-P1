# Práctico 6: Estructuras de datos complejas
# Ejercicio 7: Análisis de estudiantes que aprobaron parciales

print("=== EJERCICIO 7: ANÁLISIS DE ESTUDIANTES Y PARCIALES ===")

# Sets de estudiantes que aprobaron cada parcial
parcial_1 = {101, 102, 103, 104, 105, 106, 107}
parcial_2 = {103, 104, 105, 108, 109, 110, 111}

print("Estudiantes que aprobaron Parcial 1:")
print(sorted(parcial_1))

print("\nEstudiantes que aprobaron Parcial 2:")
print(sorted(parcial_2))

# Estudiantes que aprobaron ambos parciales (intersección)
ambos_parciales = parcial_1 & parcial_2  # También se puede usar parcial_1.intersection(parcial_2)

print(f"\n=== ESTUDIANTES QUE APROBARON AMBOS PARCIALES ===")
print(f"Cantidad: {len(ambos_parciales)}")
print(f"Estudiantes: {sorted(ambos_parciales)}")

# Estudiantes que aprobaron solo uno de los dos parciales (diferencia simétrica)
solo_uno = parcial_1 ^ parcial_2  # También se puede usar parcial_1.symmetric_difference(parcial_2)

print(f"\n=== ESTUDIANTES QUE APROBARON SOLO UNO DE LOS DOS PARCIALES ===")
print(f"Cantidad: {len(solo_uno)}")
print(f"Estudiantes: {sorted(solo_uno)}")

# Desglose: quiénes aprobaron solo el parcial 1 y quiénes solo el parcial 2
solo_parcial_1 = parcial_1 - parcial_2
solo_parcial_2 = parcial_2 - parcial_1

print(f"\nDesglose detallado:")
print(f"Solo Parcial 1: {sorted(solo_parcial_1)} (cantidad: {len(solo_parcial_1)})")
print(f"Solo Parcial 2: {sorted(solo_parcial_2)} (cantidad: {len(solo_parcial_2)})")

# Lista total de estudiantes que aprobaron al menos un parcial (unión)
al_menos_uno = parcial_1 | parcial_2  # También se puede usar parcial_1.union(parcial_2)

print(f"\n=== ESTUDIANTES QUE APROBARON AL MENOS UN PARCIAL ===")
print(f"Cantidad total: {len(al_menos_uno)}")
print(f"Estudiantes: {sorted(al_menos_uno)}")

# Verificaciones y estadísticas
print(f"\n=== VERIFICACIONES Y ESTADÍSTICAS ===")
print(f"Total estudiantes Parcial 1: {len(parcial_1)}")
print(f"Total estudiantes Parcial 2: {len(parcial_2)}")
print(f"Ambos parciales: {len(ambos_parciales)}")
print(f"Solo uno de los dos: {len(solo_uno)}")
print(f"Al menos uno: {len(al_menos_uno)}")
print(f"Verificación: {len(ambos_parciales)} + {len(solo_uno)} = {len(ambos_parciales) + len(solo_uno)} = {len(al_menos_uno)}")

# Para este ejercicio utilicé las operaciones de sets que son muy útiles para análisis de conjuntos.
# La intersección (&) me da los elementos comunes entre dos sets (ambos parciales).
# La diferencia simétrica (^) me da los elementos que están en uno u otro, pero no en ambos.
# La diferencia (-) me permite obtener elementos que están en un set pero no en el otro.
# La unión (|) me da todos los elementos únicos de ambos sets combinados.
# Los sets automáticamente eliminan duplicados, por lo que son perfectos para este tipo de análisis.
# Usé sorted() para mostrar los resultados ordenados, aunque los sets no mantienen orden.
