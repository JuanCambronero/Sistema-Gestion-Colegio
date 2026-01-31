from Personas import Personas
#Clase Alumno hereda como profesor de clase Persona
class Alumno(Personas):
    #Constructor con atributo extra grupo
    def __init__(self, id, nombre, email, grupo):
        #Hereda de Persona
        super().__init__(id, nombre, email)
        self.grupo = grupo
#Metodo personalizado heredado de Persona
    def mostrarInfo(self):
        return f"{super().mostrarInfo()} - Grupo: {self.grupo}"