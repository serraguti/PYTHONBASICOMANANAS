print("Ejemplo de Tuplas")
productos = ("Leche", "Cacao", "Avellanas", "Azucar")
print(f"Elementos de la tupla {len(productos)}")
#No podemos modificar los datos de la Tupla
productos[0] = "Leche desnatada"
for prod in productos:
    print(prod)