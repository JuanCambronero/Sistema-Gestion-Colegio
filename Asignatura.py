#Asignatura
from Profesor import Profesor

class Asignatura:
    #Constructor de Asignatura
    def __init__(self, id, nombre, profesor:Profesor, alumno: list):
        self.id= id
        self.nombre=nombre
        self.profesor=profesor
        self.alumno= []

    #getter
    @property
    def id(self):
        return self.id
    
    @property
    def nombre(self):
        return self.nombre
    
    @property
    def profesor(self):
        return self.profesor
    
    @property
    def alumno(self):
        return self.alumno
    
    #setter
    @id.setter
    def id(self,nuevo_id:int):
        self.id=nuevo_id

    @nombre.setter
    def nombre(self, nuevoNombre:str):
        self.nombre=nuevoNombre

    @profesor.setter
    def profesor(self, nuevoProfesor:str):
        self.profesor=nuevoProfesor

    @alumno.setter
    def alumno(self, nuevoAlumno:list):
        self.alumno=nuevoAlumno
    
    #Metodo para asignar Profesor
    def asignarProfesor(self,profesorAsignar:Profesor): 
        self.profesor=profesorAsignar

    #Metodo para inscribir alumno
    def inscribirAlumno(self, alumnosAsignar):
        if alumnosAsignar not in self.alumno:
            self.alumno.append(alumnosAsignar)

    #Metodo para listar alumnos
    def listar(self):
        return self.alumno

