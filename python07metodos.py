#EN UN PROGRAMA LOS METODOS DEBEN ESTAR ANTES DE LA LLAMADA
#AL METODO
def primerMetodo():
    #ESTE CODIGO NUNCA SE EJECUTARA SI NO LO LLAMAMOS
    print("Ejecutando metodo 1")
def segundoMetodo():
    print("Ejecutando metodo 2")
#---------------------------------------
#CODIGO PRINCIPAL DE NUESTRO PROGRAMA MAIN
print("Ejemplo de métodos")
#LLAMADA A LOS METODOS
primerMetodo()
segundoMetodo()
primerMetodo()
print("Fin de programa")

