#Clase colegio, esta clase sirve para gestiornar alumnos, profesores y asignaturas
import Alumno
import Profesor


class Colegio():
    #Este constructor inicia la clase recibiendo el nombre del colegio para ello
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.alumnos = {} #id - alumno
        self.profesores = {} #id - profesor
        self.asignatura = {} #id - asignatura
        self.clases = [] #listas de clases
    
    #Con este metodo añadimos un alumno a la lista de alumnos del colegio
    def addAlumno (self, alumno : Alumno):
        self.alumnos[alumno.Alumno.id] = alumno
    def addProfesor(self, profesor : Profesor):
        self.profesores[profesor.Profesor]



