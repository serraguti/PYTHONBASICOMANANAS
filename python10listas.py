print("Ejemplo de listas")
#La declaracion de una lista puede ser solo declaracion
#o agregar los objetos a su vez
listaNumeros = [12, 88, 14, 22, 16, 2]
#ORDENAR LA LISTA
#TODOS LOS METODOS MODIFICAN EL OBJETO
#ASCENDENTE
listaNumeros.sort()
listaNumeros.sort(reverse=True)
# for i in range(len(listaNumeros)):
#     print(listaNumeros[i])
#CREAMOS UNA LISTA CON NOMBRES
listaNombres = ["Adrian", "Lucia", "Carlos", "Antonia", "Diana", "Carlos"]
#LA LISTA CRECE SI AÑADIMOS DATOS
listaNombres.append("Sofia")
#PROBAMOS A INSERTAR UN NUEVO NOMBRE
#listaNombres.insert(11, "Infiltrado")
#Eliminamos un dato con Remove
# listaNombres.remove("Carlos")
#Eliminamos un dato que NO existe: Excepción
#listaNombres.remove("Carlitos")
#Probamos pop por indice
#listaNombres.pop(5)
#Si eliminamos una posicion pop que no existe?: Excepción
# listaNombres.pop(15)
print(f"La longitud de nombres es {len(listaNombres)}")
#DIBUJAMOS LOS NOMBRES CON SU POSICION
for i in range(len(listaNombres)):
    listaNombres.append("Nuevo")
    nombre = listaNombres[i]
    print(f"{i} - {nombre}")
print("----------------")
for nombre in listaNombres:
    print(nombre)
print("Fin de programa")