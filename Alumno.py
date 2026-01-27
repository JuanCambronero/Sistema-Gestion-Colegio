import Personas 

class Alumno(Personas):
    def __init__(self, id_persona: int, nombre: str, email: str, curso: str):
        super().__init__(id_persona, nombre, email)
        self.curso = curso
        self.calificaciones = {}  # asignatura_id -> lista de notas


    def id ():
        return super(id)

    def añadir_calificacion(self, id_asignatura: int, nota: float):
        self.calificaciones.setdefault(id_asignatura, []).append(nota)

    def mostrar_info(self):
        super().mostrar_info()
        print(f"  Curso: {self.curso}")