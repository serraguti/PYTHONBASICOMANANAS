print("Ejemplo de bucles")
print("Conjetura de Collatz")
numero = int(input("Introduzca un número: "))
while (numero != 1):
    if (numero % 2 == 0):
        numero = int(numero / 2)
    else:
        numero = numero * 3 + 1
    print(numero)
print("-----------------------")

#REALIZAMOS EL TIPICO BUCLE DE DIBUJAR PARES EN UN RANGO %
for i in range(20):
    #Preguntamos si un número es Par o impar
    if (i % 2 == 0):
        print(f"Par: {i}")
print("Fin de programa")