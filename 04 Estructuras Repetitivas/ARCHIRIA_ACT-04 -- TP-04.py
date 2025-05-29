# Actividad 4: Suma números hasta que se ingrese 0
# Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

print("=== ACTIVIDAD 4: SUMA HASTA CERO ===")
print("Ingrese números enteros. El programa se detendrá cuando ingrese 0.")

suma_total = 0
contador = 0

while True:
    numero = int(input(f"Número {contador + 1}: "))
    
    if numero == 0:
        print("Se ingresó 0. Finalizando...")
        break
    
    suma_total += numero
    contador += 1

print(f"\nResultados:")
print(f"Cantidad de números ingresados: {contador}")
print(f"Suma total acumulada: {suma_total}")
