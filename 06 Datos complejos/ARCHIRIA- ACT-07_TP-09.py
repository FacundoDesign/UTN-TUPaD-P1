# Práctico 6: Estructuras de datos complejas
# Ejercicio 9: Agenda con tuplas como claves

print("=== EJERCICIO 9: AGENDA CON TUPLAS COMO CLAVES ===")

# Agenda donde las claves son tuplas de (día, hora) y los valores son eventos
agenda = {
    ('Lunes', '09:00'): 'Reunión de equipo',
    ('Lunes', '14:00'): 'Almuerzo con cliente',
    ('Martes', '10:30'): 'Presentación del proyecto',
    ('Martes', '16:00'): 'Entrevista de trabajo',
    ('Miércoles', '08:00'): 'Gimnasio',
    ('Miércoles', '11:00'): 'Consulta médica',
    ('Jueves', '13:00'): 'Almuerzo familiar',
    ('Jueves', '19:00'): 'Clase de inglés',
    ('Viernes', '15:00'): 'Reunión con proveedor',
    ('Viernes', '20:00'): 'Cena con amigos'
}

print("Agenda inicial:")
print("=" * 50)
for (dia, hora), evento in sorted(agenda.items()):
    print(f"{dia} a las {hora}: {evento}")

def mostrar_menu():
    print("\n=== MENÚ DE OPCIONES ===")
    print("1. Consultar actividad en día y hora específicos")
    print("2. Agregar nueva actividad")
    print("3. Mostrar todas las actividades de un día")
    print("4. Mostrar agenda completa")
    print("5. Eliminar actividad")
    print("6. Salir")
    return input("Seleccione una opción (1-6): ").strip()

def consultar_actividad():
    dia = input("Ingrese el día (ej: Lunes): ").strip().capitalize()
    hora = input("Ingrese la hora (ej: 09:00): ").strip()
    
    # Crear la tupla clave
    clave = (dia, hora)
    
    if clave in agenda:
        evento = agenda[clave]
        print(f"✓ {dia} a las {hora}: {evento}")
    else:
        print(f"✗ No hay actividades programadas para {dia} a las {hora}")
        mostrar_horarios_disponibles(dia)

def agregar_actividad():
    dia = input("Ingrese el día (ej: Lunes): ").strip().capitalize()
    hora = input("Ingrese la hora (ej: 09:00): ").strip()
    evento = input("Ingrese el evento: ").strip()
    
    # Crear la tupla clave
    clave = (dia, hora)
    
    if clave in agenda:
        print(f"  Ya existe una actividad para {dia} a las {hora}: {agenda[clave]}")
        respuesta = input("¿Desea reemplazarla? (s/n): ").strip().lower()
        if respuesta == 's':
            agenda[clave] = evento
            print(f"✓ Actividad actualizada para {dia} a las {hora}")
        else:
            print("Operación cancelada.")
    else:
        agenda[clave] = evento
        print(f"✓ Nueva actividad agregada: {dia} a las {hora} - {evento}")

def mostrar_actividades_dia():
    dia = input("Ingrese el día (ej: Lunes): ").strip().capitalize()
    
    # Filtrar actividades del día especificado
    actividades_dia = [(hora, evento) for (d, hora), evento in agenda.items() if d == dia]
    
    if actividades_dia:
        print(f"\n=== ACTIVIDADES PARA {dia.upper()} ===")
        for hora, evento in sorted(actividades_dia):
            print(f"{hora}: {evento}")
    else:
        print(f"No hay actividades programadas para {dia}")

def mostrar_horarios_disponibles(dia):
    horarios_ocupados = [hora for (d, hora), evento in agenda.items() if d == dia]
    
    if horarios_ocupados:
        print(f"\nHorarios ocupados para {dia}:")
        for hora in sorted(horarios_ocupados):
            print(f"- {hora}")

def eliminar_actividad():
    dia = input("Ingrese el día (ej: Lunes): ").strip().capitalize()
    hora = input("Ingrese la hora (ej: 09:00): ").strip()
    
    # Crear la tupla clave
    clave = (dia, hora)
    
    if clave in agenda:
        evento = agenda[clave]
        print(f"Actividad encontrada: {dia} a las {hora} - {evento}")
        respuesta = input("¿Está seguro que desea eliminarla? (s/n): ").strip().lower()
        if respuesta == 's':
            del agenda[clave]
            print(f"✓ Actividad eliminada: {dia} a las {hora}")
        else:
            print("Operación cancelada.")
    else:
        print(f"✗ No hay actividades programadas para {dia} a las {hora}")

def mostrar_agenda_completa():
    print("\n=== AGENDA COMPLETA ===")
    print(f"Total de actividades: {len(agenda)}")
    print("=" * 50)
    
    # Agrupar por día
    dias = {}
    for (dia, hora), evento in agenda.items():
        if dia not in dias:
            dias[dia] = []
        dias[dia].append((hora, evento))
    
    # Mostrar ordenado por día y hora
    for dia in sorted(dias.keys()):
        print(f"\n{dia.upper()}:")
        for hora, evento in sorted(dias[dia]):
            print(f"  {hora}: {evento}")

# Bucle principal del programa
while True:
    opcion = mostrar_menu()
    
    if opcion == '1':
        consultar_actividad()
    elif opcion == '2':
        agregar_actividad()
    elif opcion == '3':
        mostrar_actividades_dia()
    elif opcion == '4':
        mostrar_agenda_completa()
    elif opcion == '5':
        eliminar_actividad()
    elif opcion == '6':
        print("¡Gracias por usar la agenda!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 6.")

# Para este ejercicio utilicé tuplas como claves del diccionario, lo cual es muy útil para crear claves compuestas.
# Las tuplas son inmutables, por lo que pueden usarse como claves en diccionarios (a diferencia de las listas).
# Implementé múltiples funciones para hacer el programa más modular y fácil de mantener.
# Usé list comprehension para filtrar actividades por día específico.
# El método .items() me permite iterar sobre las tuplas-clave y valores simultáneamente.
# La función sorted() funciona correctamente con tuplas, ordenando primero por el primer elemento y luego por el segundo.
# Agregué validación y confirmación para operaciones críticas como eliminar actividades.
