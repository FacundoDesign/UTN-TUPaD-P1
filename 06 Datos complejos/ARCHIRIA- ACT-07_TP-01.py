# Práctico 6: Estructuras de datos complejas
# Ejercicio 1: Agregar frutas al diccionario

print("=== EJERCICIO 1: AGREGAR FRUTAS AL DICCIONARIO ===")

# Diccionario inicial de precios de frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

print("Diccionario inicial:")
print(precios_frutas)

# Agregar las nuevas frutas con sus respectivos precios
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("\nDiccionario después de agregar las nuevas frutas:")
print(precios_frutas)

print(f"\nTotal de frutas en el diccionario: {len(precios_frutas)}")

# Para este ejercicio usé la sintaxis de diccionarios con corchetes [] para agregar nuevas claves y valores.
# Los diccionarios en Python permiten agregar elementos simplemente asignando un valor a una nueva clave.
# El método len() me permite verificar cuántos elementos tiene el diccionario después de las adiciones.
