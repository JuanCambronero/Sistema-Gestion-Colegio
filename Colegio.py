#Clase colegio, esta clase sirve para gestiornar alumnos, profesores y asignaturas
import Alumno
import Profesor
import Alumno
import Profesor

class Colegio:

    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = {} 
        self.profesores = {} 
        self.asignatura = {} 
        self.clases = [] 

    # GESTIÓN ALUMNOS
    def addAlumno (self, alumnoAdd : Alumno.Alumno):
        self.alumnos[alumnoAdd.idPersona] = alumnoAdd

    def eliminarAlumno(self, idEliminar):
        self.alumnos.pop(idEliminar, None)

    def buscarAlumno (self, idBusqueda):
        alumno = self.alumnos.get(idBusqueda)
        if alumno:
            print(Alumno.Alumno.mostrar_info(alumno))
        else:
            print("Alumno NO encontrado")
    
    def listarAlumnos (self):
        for id , alumno in self.alumnos.values:
            print(f"{id} : {Alumno.Alumno.mostrar_info(alumno)}")

    # GESTIÓN PROFESORES  
    def addProfesor(self, profesor : Profesor.Profesor):
        self.profesores[profesor.idPersona] = profesor

    def eliminarProfesor(self, idEliminar):
        self.profesores.pop(idEliminar, None)



