# Práctico 6: Estructuras de datos complejas
# Ejercicio 10: Invertir diccionario países-capitales

print("=== EJERCICIO 10: INVERTIR DICCIONARIO PAÍSES-CAPITALES ===")

# Diccionario original que mapea países con sus capitales
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasília',
    'Chile': 'Santiago',
    'Uruguay': 'Montevideo',
    'Paraguay': 'Asunción',
    'Bolivia': 'Sucre',
    'Perú': 'Lima',
    'Ecuador': 'Quito',
    'Colombia': 'Bogotá',
    'Venezuela': 'Caracas',
    'Francia': 'París',
    'España': 'Madrid',
    'Italia': 'Roma',
    'Alemania': 'Berlín',
    'Reino Unido': 'Londres'
}

print("Diccionario original (Países → Capitales):")
print("=" * 50)
for pais, capital in sorted(paises_capitales.items()):
    print(f"{pais}: {capital}")

# Construir el nuevo diccionario donde las capitales son claves y los países son valores
capitales_paises = {}

for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print(f"\nDiccionario invertido (Capitales → Países):")
print("=" * 50)
for capital, pais in sorted(capitales_paises.items()):
    print(f"{capital}: {pais}")

# Verificaciones y estadísticas
print(f"\n=== VERIFICACIONES ===")
print(f"Cantidad de países en diccionario original: {len(paises_capitales)}")
print(f"Cantidad de capitales en diccionario invertido: {len(capitales_paises)}")
print(f"Los tamaños coinciden: {len(paises_capitales) == len(capitales_paises)}")

# Función para consultar país por capital
def consultar_pais_por_capital():
    capital = input("\nIngrese el nombre de una capital: ").strip()
    
    if capital in capitales_paises:
        pais = capitales_paises[capital]
        print(f"✓ {capital} es la capital de {pais}")
    else:
        print(f"✗ {capital} no se encuentra en la base de datos")
        print("Capitales disponibles:")
        for cap in sorted(capitales_paises.keys()):
            print(f"- {cap}")

# Función para consultar capital por país
def consultar_capital_por_pais():
    pais = input("\nIngrese el nombre de un país: ").strip()
    
    if pais in paises_capitales:
        capital = paises_capitales[pais]
        print(f"✓ La capital de {pais} es {capital}")
    else:
        print(f"✗ {pais} no se encuentra en la base de datos")
        print("Países disponibles:")
        for p in sorted(paises_capitales.keys()):
            print(f"- {p}")

# Demostración de las funciones
print(f"\n=== DEMOSTRACIÓN DE CONSULTAS ===")

# Consulta de ejemplo 1: Capital → País
print("\nEjemplo 1: Consulta por capital")
print("Capital: Buenos Aires")
if 'Buenos Aires' in capitales_paises:
    print(f"País: {capitales_paises['Buenos Aires']}")

# Consulta de ejemplo 2: País → Capital
print("\nEjemplo 2: Consulta por país")
print("País: Francia")
if 'Francia' in paises_capitales:
    print(f"Capital: {paises_capitales['Francia']}")

# Mostrar ambos diccionarios de forma comparativa
print(f"\n=== COMPARACIÓN LADO A LADO ===")
print(f"{'PAÍS':<15} {'CAPITAL':<15} {'CAPITAL':<15} {'PAÍS':<15}")
print("=" * 60)

for pais, capital in sorted(paises_capitales.items()):
    pais_invertido = capitales_paises[capital]
    print(f"{pais:<15} → {capital:<15} || {capital:<15} → {pais_invertido:<15}")

# Menú interactivo para consultas
print(f"\n=== CONSULTAS INTERACTIVAS ===")
while True:
    print("\nOpciones:")
    print("1. Consultar país por capital")
    print("2. Consultar capital por país")
    print("3. Salir")
    
    opcion = input("Seleccione una opción (1-3): ").strip()
    
    if opcion == '1':
        consultar_pais_por_capital()
    elif opcion == '2':
        consultar_capital_por_pais()
    elif opcion == '3':
        print("¡Gracias por usar el consultor de países y capitales!")
        break
    else:
        print("Opción inválida. Por favor, seleccione 1, 2 o 3.")

# Para este ejercicio invertí un diccionario intercambiando claves y valores.
# Utilicé el método .items() para iterar sobre pares clave-valor del diccionario original.
# Creé un nuevo diccionario donde las capitales (valores originales) se convierten en claves.
# Implementé funciones de consulta bidireccional para demostrar la utilidad de ambos diccionarios.
# Agregué verificaciones para asegurar que la inversión se realizó correctamente.
# El menú interactivo permite al usuario probar las consultas en ambas direcciones.
# La comparación lado a lado muestra claramente cómo se invirtieron las relaciones.
