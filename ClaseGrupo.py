from Profesor import Profesor
from Alumno import Alumno  
#Esta clase simula unpromoción de alumnos frmada por alumnos y tutor
class ClaseGrupo:
    #Constructor con los atributos
    def __init__(self, id, nombre, tutor: Profesor = None):
        self.id = id
        self.nombre = nombre
        self.tutor = tutor
        self.alumnos = [] 
    #Metodo para asignar Alumnos a la promoción
    def addAlumno(self, alumno: Alumno):
        self.alumnos.append(alumno)
    #Metodo para asignar al Tutor de la promoción
    def asignarTutor(self, tutor: Profesor):
        self.tutor = tutor
    #Recoje a todos los alumnos que forman la promoción
    def getAlumnos(self):
        return self.alumnos
    #Muestra los datos de la promoción
    def mostarInfo(self):
        tutorNombre = self.tutor.obtener_nombre() if self.tutor else "Sin"
        return f"Grupo {self.nombre} (Tutor: {tutorNombre}, Alumnos: {len(self.alumnos)})"

