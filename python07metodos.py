#EN UN PROGRAMA LOS METODOS DEBEN ESTAR ANTES DE LA LLAMADA
#AL METODO
def primerMetodo():
    #ESTE CODIGO NUNCA SE EJECUTARA SI NO LO LLAMAMOS
    print("Ejecutando metodo 1")
def segundoMetodo():
    print("Ejecutando metodo 2")
def saludar(nombre):
    print(f"Hola en Python {nombre}")
def despedirse(nombre, dia):
    print(f"Hasta luego {nombre} en el día {dia}")
#---------------------------------------
#CODIGO PRINCIPAL DE NUESTRO PROGRAMA MAIN
print("Ejemplo de métodos")
saludar("Paco")
despedirse("Paco", "Martes")
#saludar("Paco")
#LLAMADA A LOS METODOS
primerMetodo()
segundoMetodo()
primerMetodo()
print("Fin de programa")

