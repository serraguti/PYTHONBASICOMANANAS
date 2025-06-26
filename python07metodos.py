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
#METODO DE ACCION
def mostrarMenu():
    print("Seleccione una opcion")
    print("1.- Convertir mayusculas")
    print("2.- Convertir minusculas")
#METODOS RETURN
def convertirMayusculas(texto):
    #TODO NUESTRO CODIGO
    return texto.upper()

def convertirMinusculas(texto):
    return texto.lower()
#---------------------------------------
#CODIGO PRINCIPAL DE NUESTRO PROGRAMA MAIN
print("Ejemplo de métodos")
mostrarMenu()
#EN LA LLAMADA DEBEMOS CAPTURAR EL VALOR DEVUELTO
respuesta = convertirMayusculas("juernes de pyThON")
print(respuesta)
# saludar("Paco")
# despedirse("Paco", "Martes")
#saludar("Paco")
#LLAMADA A LOS METODOS
# primerMetodo()
# segundoMetodo()
# primerMetodo()
print("Fin de programa")

