def sumarNumeros(num1, num2):
    return num1 + num2

def multiplicarNumeros(num1, num2):
    return num1 * num2

def mostrarMenu():
    print("0.- Salir")
    print("1.- Sumar")
    print("2.- Multiplicar")
    print("3.- Introduzca nuevos numeros")
    print("Seleccione una opcion")

#-----------------PRINCIPAL-------------------
print("Calculadora métodos")
numero1 = int(input("Introduzca numero 1: "))
numero2 = int(input("Introduzca numero 2: "))
opcion = 1
while (opcion != 0):
    mostrarMenu()
    opcion = int(input())
    if (opcion == 1):
        suma = sumarNumeros(numero1, numero2)
        print(f"La suma de {numero1} y {numero2} es {suma}")
    elif (opcion == 2):
        multi = multiplicarNumeros(numero1, numero2)
        print(f"{numero1} * {numero2} = {multi}")
print("Fin de programa")