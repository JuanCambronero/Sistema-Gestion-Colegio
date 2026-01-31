from Personas import Personas
#Clase Profesor hereda de clase persona
class Profesor(Personas):
    #Constructor con atributo extra departamento
    def __init__(self, id, nombre, email, departamento):
        #Herencia de Persona
        super().__init__(id, nombre, email)
        self.departamento = departamento
        self.asignaturas = []
#Este metodo asigna las asignaturas que imparte el profesor
    def addAsignatura(self, asignatura_id):
        self.asignaturas.append(asignatura_id)
#Metodo personalizado heredado de Persona
    def mostrarInfo(self):
        return f"Departamento: {self.departamento}, Asignaturas: {self.asignaturas}"


