#el acceso a las librerías se escribe al inicio
from math import pow

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

def getComprobarNumero():
    print("Introduzca un numero")
    aux = input()
    while (aux.isdigit() == False):
        print("Esto no es un numero")
        print("Introduzca un numero")
        aux = input()
    num = int(aux)
    return num
#-----------------PRINCIPAL-------------------
print("Calculadora métodos")
numero1 = getComprobarNumero()
numero2 = getComprobarNumero()
potencia = pow(numero1, numero2)
print(potencia)
# opcion = 1
# while (opcion != 0):
#     mostrarMenu()
#     opcion = int(input())
#     if (opcion == 1):
#         suma = sumarNumeros(numero1, numero2)
#         print(f"La suma de {numero1} y {numero2} es {suma}")
#     elif (opcion == 2):
#         multi = multiplicarNumeros(numero1, numero2)
#         print(f"{numero1} * {numero2} = {multi}")
#     elif (opcion == 3):
#         numero1 = getComprobarNumero()
#         numero2 = getComprobarNumero()
print("Fin de programa")