from models.persona import Persona
from models.empleado import Empleado
from models.director import Director

print("Utilizando clases Persona")
empleado = Empleado()
empleado.nombre = "Marcos "
empleado.apellidos = "Lopez Ramos"
print(empleado)

dire = Director()
# print(f"Vacaciones empleado: {empleado.getVacaciones()}")
# print(f"Vacaciones director: {dire.getVacaciones()}")

# #HEMOS DICHO QUE UNA PERSONA ES DE FRANCIA SIEMPRE
# #UN EMPLEADO ES UNA PERSONA, VERDAD?
# #UN EMPLEADO DEBE SER TAMBIEN DE FRANCIA O NO?
# # empleado.pais = "Spain"
# print(f"Pais empleado: {empleado.pais}")
# empleado.nombre = "Empleado "
# empleado.apellidos = "del mes"
# print(empleado.getNombreCompleto())
# print(f"Vacaciones empleado: {empleado.getVacaciones()}")
# print(f"Sueldo empleado: {empleado.salario}")
# personaje = Persona()
# print(personaje.pais)
# personaje.nombre = "Sheldon"
# personaje.apellidos = "Cooper"
# personaje.edad = 44
# personaje.pais = "EEUU"
# print(personaje.getDatoPrivado())
# print(personaje.getNombreCompleto(22))
# print(personaje.getNombreCompletoReves())
# print(f"Nombre: {personaje.nombre}, Apellidos: {personaje.apellidos}")

