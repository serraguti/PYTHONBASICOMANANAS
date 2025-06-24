print("Ejemplo de variables")
numero = 14
texto = "Primer Python"
#Comentarios en Python
#Comentar dentro de VS Code
#Comentar: CONTROL + K + C 
#Descomentar: CONTROL + K + U
print(numero)
print(texto)
#El simbolo + sirve para concatenar y también para sumar
#Verifica el tipo de dato
print("Texto: " + texto)
#print("Numero: " + numero)
#También podemos utilizar la coma para concatenar
print("Numero: ", numero)
#print f nos permite concatenar múltiples variables en String sin 
#importar el tipo de dato.
#Cada variable lógica debe ir entre llaves {}
#La letra f se escribe ANTES del String y fuera del string
print(f"El texto es {texto} y el número es {numero}")
#Dentro de las variables primitivas: str, int, boolean, float
#podemos convertir mediante funciones de Python
#str(variable): Convierte un tipo a String
#int(variable): Convierte un tipo a Entero
#float(variable): Convierte un tipo a Decimal
print("Numero: " + str(numero))
