from models.persona import Persona
print("Utilizando clases Persona")
personaje = Persona()
print(personaje.pais)
personaje.nombre = "Sheldon"
personaje.apellidos = "Cooper"
personaje.edad = 44
personaje.pais = "EEUU"
print(personaje.getDatoPrivado())
print(personaje.getNombreCompleto(22))
# print(personaje.getNombreCompletoReves())
print(f"Nombre: {personaje.nombre}, Apellidos: {personaje.apellidos}")

