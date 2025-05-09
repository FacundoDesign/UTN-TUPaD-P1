#Práctico 3: Estructuras condicionales

#Actividad 9

# Programa que clasifica terremotos según la escala de Richter
magnitud = float(input("Ingrese la magnitud del terremoto en la escala Richter: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:  # magnitud >= 7
    print("Extremo (puede causar graves daños a gran escala)")

#Otro ejemplo de uso de múltiples condiciones para clasificar la magnitud del terremoto en diferentes categorías.
