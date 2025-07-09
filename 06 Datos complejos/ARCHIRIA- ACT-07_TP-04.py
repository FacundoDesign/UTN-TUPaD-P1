# Práctico 6: Estructuras de datos complejas
# Ejercicio 4: Agenda telefónica

print("=== EJERCICIO 4: AGENDA TELEFÓNICA ===")

# Diccionario para almacenar contactos
agenda = {}

# Permitir al usuario cargar 5 contactos
print("Ingrese 5 contactos:")
for i in range(5):
    print(f"\nContacto {i + 1}:")
    nombre = input("Nombre: ").strip()
    telefono = input("Número de teléfono: ").strip()
    
    # Agregar el contacto al diccionario
    agenda[nombre] = telefono
    print(f"Contacto {nombre} agregado correctamente.")

# Mostrar la agenda completa
print(f"\n=== AGENDA COMPLETA ===")
print(f"Total de contactos: {len(agenda)}")
for nombre, telefono in agenda.items():
    print(f"{nombre}: {telefono}")

# Consultar un contacto
print(f"\n=== CONSULTA DE CONTACTO ===")
nombre_buscar = input("Ingrese el nombre del contacto a buscar: ").strip()

# Verificar si el contacto existe
if nombre_buscar in agenda:
    print(f"El número de {nombre_buscar} es: {agenda[nombre_buscar]}")
else:
    print(f"El contacto '{nombre_buscar}' no se encuentra en la agenda.")
    
# Mostrar contactos disponibles si no se encuentra
if nombre_buscar not in agenda:
    print("Contactos disponibles:")
    for nombre in agenda.keys():
        print(f"- {nombre}")

# Para este ejercicio utilicé un diccionario donde las claves son los nombres y los valores son los números.
# Usé un bucle for para permitir la carga de 5 contactos de manera ordenada.
# El método .items() me permite iterar sobre claves y valores simultáneamente.
# La verificación de existencia con 'in' me permite consultar si un contacto existe antes de mostrarlo.
# El método .strip() elimina espacios en blanco al inicio y final de las entradas del usuario.
