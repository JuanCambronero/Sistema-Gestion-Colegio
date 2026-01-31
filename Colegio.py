#Clase colegio, esta clase sirve para gestiornar alumnos, profesores y asignaturas
import Alumno
import Profesor
import ClaseGrupo

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
            print(Alumno.Alumno.mostrarInfo(alumno))
        else:
            print("Alumno NO encontrado")
    
    def listarAlumnos(self):
        for id, alumno in self.alumnos.items():
            print(f"{id} : {alumno.mostrarInfo()}")



    # GESTIÓN PROFESORES  
    def addProfesor(self, profesor : Profesor.Profesor):
        self.profesores[profesor.idPersona] = profesor

    def eliminarProfesor(self, idEliminar):
        self.profesores.pop(idEliminar, None)
    
    def buscarProfesor (self, idBusqueda):
        profesor = self.profesores.get(idBusqueda)
        if profesor:
            print(Profesor.Profesor.mostrarInfo(profesor))
        else:
            print("Profesor NO encontrado")
    
    def listarProfesores(self):
        for id, profe in self.profesores.items():
            print(f"{id} : {profe.mostrarInfo()}")

    #GESTIÓN DE CLASES
    def addClaseGrupo(self, claseGrupo : ClaseGrupo.ClaseGrupo ):
        self.clases.append(claseGrupo)

    def buscarClase(self, idBusqueda):
        for c in self.clases:
            if c.id == idBusqueda:
                return c
        return None


