from abc import ABC, abstractmethod
#Clase abstarcta que representa los atributos minimos que debe tener una persona en el sistema
class Personas(ABC):
    #Constructor con los atributos esenciales
    def __init__(self, id: int, nombre: str, email: str):
        self.idPersona = id
        self.nombre = nombre
        self.email = email
#GETTERS
    def obtener_id(self) -> int:
        return self.idPersona

    def obtener_nombre(self) -> str:
        return self.nombre

    def obtener_email(self) -> str:
        return self.email

    def mostrar_info(self) -> str:
        return f"ID: {self.idPersona}, Nombre: {self.nombre}, Email: {self.email}"
#Este metodo se debe personalizar en cada clase
    @abstractmethod
    def mostrarInfo(self) -> str:
        pass
