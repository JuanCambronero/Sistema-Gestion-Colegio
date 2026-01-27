import Personas

class Alumno(Personas.Personas):
    #CONSTRUCTOR
    def __init__(self, id_persona: int, nombre: str, email: str, curso: str):
        super().__init__(id_persona, nombre, email) 
        self.curso = curso
        self.calificaciones = {}  # id_asignatura → lista notas
    
    def id(self):  
        return super().obtener_id()
    
    def mostrar_info(self):
        super().mostrar_info()  # Info de Personas
        print(f"  Curso: {self.curso}")
        print(f"  Calificaciones: {len(self.calificaciones)} asignaturas")

