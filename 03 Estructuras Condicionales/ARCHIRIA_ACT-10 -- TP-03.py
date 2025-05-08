#Práctico 3: Estructuras condicionales 
#Actividad 10


# Programa que determina la estación del año
hemisferio = input("¿En qué hemisferio se encuentra? (N para Norte, S para Sur): ").upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes (1-31): "))

# Determinar el periodo del año
if (mes == 12 and dia >= 21) or (mes <= 3 and (mes != 3 or dia <= 20)):
    # Del 21 de diciembre al 20 de marzo
    if hemisferio == "N":
        estacion = "Invierno"
    else:
        estacion = "Verano"
elif (mes == 3 and dia >= 21) or (mes <= 6 and (mes != 6 or dia <= 20)):
    # Del 21 de marzo al 20 de junio
    if hemisferio == "N":
        estacion = "Primavera"
    else:
        estacion = "Otoño"
elif (mes == 6 and dia >= 21) or (mes <= 9 and (mes != 9 or dia <= 20)):
    # Del 21 de junio al 20 de septiembre
    if hemisferio == "N":
        estacion = "Verano"
    else:
        estacion = "Invierno"
else:  # Del 21 de septiembre al 20 de diciembre
    if hemisferio == "N":
        estacion = "Otoño"
    else:
        estacion = "Primavera"

print(f"La estación actual es: {estacion}")
