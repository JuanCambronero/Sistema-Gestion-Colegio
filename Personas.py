from abc import ABC, abstractmethod
#Clase abstarcta que representa los atributos minimos que debe tener una persona en el sistema
class Personas(ABC):
    #Constructor con los atributos esenciales
    def __init__(self, id, nombre, email):
        self.idPersona = id
        self.nombre = nombre
        self.email = email
#GETTERS
    def obtener_id(self):
        return self.idPersona

    def obtener_nombre(self):
        return self.nombre

    def obtener_email(self):
        return self.email

    def mostrar_info(self):
        return f"ID: {self.idPersona}, Nombre: {self.nombre}, Email: {self.email}"
    #Este metodo se debe personalizar en cada clase
    @abstractmethod
    def mostrarInfo(self) -> str:
        pass
