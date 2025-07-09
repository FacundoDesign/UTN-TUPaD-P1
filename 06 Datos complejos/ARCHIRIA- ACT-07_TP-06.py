# Práctico 6: Estructuras de datos complejas
# Ejercicio 6: Promedio de notas de alumnos

print("=== EJERCICIO 6: PROMEDIO DE NOTAS DE ALUMNOS ===")

# Diccionario para almacenar alumnos y sus notas
alumnos_notas = {}

# Permitir ingresar los nombres de 3 alumnos y sus notas
print("Ingrese los datos de 3 alumnos:")

for i in range(3):
    print(f"\nAlumno {i + 1}:")
    nombre = input("Nombre del alumno: ").strip()
    
    # Solicitar las 3 notas
    print(f"Ingrese las 3 notas de {nombre}:")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    
    # Crear una tupla con las 3 notas
    notas_tupla = (nota1, nota2, nota3)
    
    # Agregar el alumno y sus notas al diccionario
    alumnos_notas[nombre] = notas_tupla
    
    print(f"Notas de {nombre} registradas: {notas_tupla}")

# Mostrar el promedio de cada alumno
print(f"\n=== PROMEDIOS DE ALUMNOS ===")

for nombre, notas in alumnos_notas.items():
    # Calcular el promedio de las notas en la tupla
    promedio = sum(notas) / len(notas)
    
    print(f"Alumno: {nombre}")
    print(f"Notas: {notas}")
    print(f"Promedio: {promedio:.2f}")
    
    # Determinar si aprobó o no (asumiendo que se aprueba con 6 o más)
    if promedio >= 6:
        print(f"Estado: APROBADO ✓")
    else:
        print(f"Estado: DESAPROBADO ✗")
    print("-" * 30)

# Mostrar estadísticas generales
print(f"\n=== ESTADÍSTICAS GENERALES ===")
todos_promedios = [sum(notas) / len(notas) for notas in alumnos_notas.values()]
promedio_general = sum(todos_promedios) / len(todos_promedios)

print(f"Promedio general del curso: {promedio_general:.2f}")
print(f"Promedio más alto: {max(todos_promedios):.2f}")
print(f"Promedio más bajo: {min(todos_promedios):.2f}")

# Para este ejercicio utilicé un diccionario donde las claves son los nombres de los alumnos.
# Los valores son tuplas que contienen las 3 notas de cada alumno.
# Las tuplas son ideales para almacenar las notas porque son inmutables y ordenadas.
# Usé la función sum() para sumar todos los elementos de la tupla y len() para obtener la cantidad.
# La función .items() me permite iterar sobre nombres y tuplas de notas simultáneamente.
# Implementé list comprehension para crear una lista de todos los promedios y calcular estadísticas.
