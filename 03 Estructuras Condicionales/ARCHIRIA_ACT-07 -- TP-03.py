#Práctico 3: Estructuras condicionales

#Actividad 7

# Programa que modifica el string según su terminación
frase = input("Ingrese una frase o palabra: ")

# Verificar si termina con vocal
ultima_letra = frase[-1].lower()  # Obtener última letra y convertirla a minúscula
vocales = "aeiou"

if ultima_letra in vocales:
    frase = frase + "!"
    
print(frase)

#Para este ejercicio tuve que verificar si la última letra era una vocal. 
#Usé frase[-1] para obtener el último carácter y la técnica de pertenencia "in" para verificar si estaba en mi lista de vocales.
