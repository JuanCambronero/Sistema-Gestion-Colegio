from Personas import Personas
#Clase Alumno hereda como profesor de clase Persona
class Alumno(Personas):
    #Constructor con atributo extra grupo
    def __init__(self, id: int, nombre: str, email: str, grupo: str):
        #Hereda de Persona
        super().__init__(id, nombre, email)
        self.grupo = grupo
#Metodo personalizado heredado de Persona
    def mostrarInfo(self) -> str:
        return f"Grupo: {self.grupo}"