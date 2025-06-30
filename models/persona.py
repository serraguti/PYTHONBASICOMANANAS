class Persona:
    #TENEMOS DOS FORMAS DE DECLARAR PROPIEDADES
    #PARA LA PERSONA
    #1) AL INICIO DE LA CLASE
    # nombre = ""
    # apellidos = ""
    # edad = 0
    # pais = ""
    def __init__(self):
        # tenemos la posibilidad de crear propiedades privadas
        # las propiedades privadas solamente se pueden utilizar dentro
        # de la clase Persona y se definen mediante dos guiones bajos:
        # __propiedadPrivada
        self.__datoPrivado = "Esto no lo vas a ver Python..."
        self.nombre = ""
        self.apellidos = ""
        self.edad = 0
        self.pais = "Francia"
    
    def getDatoPrivado(self):
        return self.__datoPrivado
    
    #CREAMOS UN METODO QUE NOS DEVUELVA EL NOMBRE COMPLETO DE UNA PERSONA
    def getNombreCompleto(self):
        return self.nombre + " " + self.apellidos

    #imaginemos que tenemos un método que deseamos que nos 
    #devuelva el nombre completo, pero deseamos que lo realice
    #al reves, apellidos y nombre
    # def getNombreCompleto(self, reves):
    #     return self.apellidos + " " + self.nombre