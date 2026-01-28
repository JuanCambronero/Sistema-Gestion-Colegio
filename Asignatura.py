#Esta clase simula una asignatura formada por profesor y alumnos

class Asignatura:
    #Constructor con los atribustos de la clase
    def __init__(self, id: str, nombre: str):
        self.id = id
        self.nombre = nombre
        self.profesor_id = None
        self.alumnos_ids = []
    #Metodo para asignar x profesor a la asignatura 
    def asignar_profesor(self, profesorAsignar: str):
        self.profesor_id = profesorAsignar
    #Metodo para añadir alumnos inscritos a la asignatura
    def inscribir_alumno(self, alumno_id: int):
        if alumno_id not in self.alumnos_ids:
            self.alumnos_ids.append(alumno_id)
    #Metodo que muestra quienes estan inscritos a la asinatura
    def mostrarInfo(self):
        return f"Asignatura {self.nombre} (Prof: {self.profesor_id}, Alumnos: {len(self.alumnos_ids)})"


