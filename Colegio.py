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
        self.clases = [] #listas de clases del colegio

    #GESTIÓN ALUMNOS
    def addAlumno (self, alumno : Alumno):
        self.alumnos[alumno.Alumno.id] = alumno
    def eliminarAlumno(self, idElimiar):
        self.alumnos.pop(idElimiar)
    def buscarAlumno (self, alumnoMostrar:Alumno, idBusqueda):
        alumnoMostrar = self.alumnos[idBusqueda]
        print(alumnoMostrar.Alumno.mostrar_info())

    #GESTIÓN PROFESORES
    def addProfesor(self, profesor : Profesor):
        self.profesores[profesor.Profesor]
    def eliminarProfesor(self, idEliminar):
        self.profesores.pop(idEliminar)



