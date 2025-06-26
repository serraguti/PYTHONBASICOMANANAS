print("Ejemplo de diccionarios")
#CREAMOS EL DICCIONARIO DE PROVINCIAS
provincias = dict()
provincias = {
    924 : "Badajoz",
    956:  "Cádiz",
    958 : "Granada",
    959 : "Huelva"
}
#AGREGAMOS UNA NUEVA PROVINCIA
provincias.setdefault(33, "Oviedo")
#QUE SUCEDE SI YA EXISTE¿¿?? NO LO INSERTA
provincias.setdefault(959, "Oviedo")
provincias.pop(959)
print(f"Longitud de Keys en diccionario: {len(provincias)}")
for key, value in provincias.items():
    print(f"{key}: {value}")
print("Fin de programa")
