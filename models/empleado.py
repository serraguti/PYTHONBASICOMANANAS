from models.persona import Persona

class Empleado(Persona):
    #AHORA MISMO EL EMPLEADO TIENE LAS MISMAS 
    #CARACTERISTICAS QUE UNA PERSONA
    #AÑADIMOS ALGO QUE NO TENGA UNA PERSONA
    def __init__(self):
        super().__init__()
        self.salario = 1700

    #PODEMOS CREAR METODOS QUE NO TENGA UNA PERSONA
    def getVacaciones(self):
        return 22