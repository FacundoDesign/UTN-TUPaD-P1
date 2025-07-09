# Práctico 6: Estructuras de datos complejas
# Ejercicio 3: Crear lista con nombres de frutas

print("=== EJERCICIO 3: CREAR LISTA CON NOMBRES DE FRUTAS ===")

# Diccionario resultante del ejercicio anterior
precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 
                  'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

print("Diccionario completo:")
print(precios_frutas)

# Crear una lista que contenga únicamente las frutas (claves) sin los precios
lista_frutas = list(precios_frutas.keys())

print(f"\nLista de frutas (solo nombres):")
print(lista_frutas)

# Mostrar información adicional
print(f"\nTotal de frutas: {len(lista_frutas)}")
print("Frutas en orden alfabético:")
frutas_ordenadas = sorted(lista_frutas)
print(frutas_ordenadas)

# Para este ejercicio utilicé el método .keys() que devuelve las claves del diccionario.
# Como keys() devuelve un objeto dict_keys, lo convertí a lista usando list().
# También apliqué la función sorted() para mostrar las frutas en orden alfabético.
# El método len() me permite contar cuántas frutas hay en la lista.
