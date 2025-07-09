# Práctico 6: Estructuras de datos complejas
# Ejercicio 2: Actualizar precios de frutas

print("=== EJERCICIO 2: ACTUALIZAR PRECIOS DE FRUTAS ===")

# Diccionario resultante del ejercicio anterior
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 
                  'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

print("Diccionario antes de actualizar precios:")
print(precios_frutas)

# Actualizar los precios de las frutas especificadas
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("\nDiccionario después de actualizar precios:")
print(precios_frutas)

# Mostrar los cambios realizados
print("\n=== CAMBIOS REALIZADOS ===")
print("Banana: 1200 → 1330 (incremento de 130)")
print("Manzana: 1500 → 1700 (incremento de 200)")
print("Melón: 3000 → 2800 (reducción de 200)")

# Para este ejercicio utilicé la misma sintaxis que para agregar elementos, pero aplicada a claves existentes.
# En Python, si una clave ya existe en el diccionario, asignarle un nuevo valor actualiza el valor existente.
# Los diccionarios son mutables, por lo que permiten modificar sus valores después de ser creados.
