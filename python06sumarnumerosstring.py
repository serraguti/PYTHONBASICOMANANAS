print("Sumar numeros textos")
textoNumeros = input("Introduzca solo numeros: ")
suma = 0
#1234
#Realizamos un bucle para recorrer cada letra del texto String
for i in range(len(textoNumeros)):
    #recuperamos cada letra de cada posicion textoNumero[posicion]
    letra = textoNumeros[i] # "1"
    #convertimos el caracter "1" a int 1
    numero = int(letra)
    suma = suma + numero
print(f"La suma de {textoNumeros} es {suma}")
print("Fin de programa")


