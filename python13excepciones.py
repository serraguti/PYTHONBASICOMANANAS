import sys
def controlExcepciones():
    try:
        numero1 = int(input("Introduzca un numero 1: "))
        numero2 = int(input("Introduzca un numero 2: "))
        resultado = numero1 / numero2
        print(f"El resultado es {resultado}")
    except:
        print(f"Error en programa: {sys.exc_info()}")

print("Control de excepciones")
controlExcepciones()
print("Fin de programa")