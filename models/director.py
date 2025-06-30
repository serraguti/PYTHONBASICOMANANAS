from models.empleado import Empleado

class Director(Empleado):
    def mandar(self):
        print("Soy el amo de todo!!!")

    def getVacaciones(self):
        #Necesitamos el código del método super
        #capturamos las vacaciones del empleado
        vacas = super().getVacaciones()
        return vacas + 8