
#Este le hace raul

#Hago la clase grupo (Jaime)

from typing import List
from Profesor import Profesor
from Alumno import Alumno

class ClaseGrupo:
    def __init__(self, id: int, nombre: str, tutor:"Profesor" =None):
         #Voy a colocar los atributos de la clase grupo
        self.id: int = id
        self.nombre: str = nombre
        self.tutor: "Profesor" = tutor
        self.alumnos: List= [] #En la imagen del uml aparece que coge valores de la clase alumno

#Hago los metodos de esta clase para poder trabajar luego con el grupo

def addAlumno(self, alumnos:Alumno) :
    self.alumnos.append(alumnos)#alumno: "Alumno" indica que el parametro alumno debe ser un objeto de la clase Alumno

def asignaturaTutor(self, profesor :"Profesor") -> None:
    self.tutor= profesor #asigna un tutor a una clase

    #  getters
    def get_id(self) -> int:
        return self.id

    def get_nombre(self) -> str:
        return self.nombre

    def get_tutor(self) -> Profesor | None:
        return self.tutor

    def get_alumnos(self) -> List[Alumno]:
        return self.alumno

    # setters
    def set_id(self, id: int) -> None:
        self.id = id

    def set_nombre(self, nombre: str) -> None:
        self.nombre = nombre

    def set_tutor(self, profesor: Profesor | None) -> None:
        self.tutor = profesor

    def set_alumnos(self, alumnos: List[Alumno]) -> None:
        self.alumno = alumnos


