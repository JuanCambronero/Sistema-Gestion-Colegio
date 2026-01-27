# Clase abstracta Persona 
class Personas:
    #CONSTRUCTOR
    def __init__(self, id: int, nombre: str, email: str):
        self.idPersona = id
        self.nombre = nombre.strip()
        self.email = email.strip()

    # SETTERS 
    def idPersona(self, id: int) -> None:
        # Asigna el id a la persona
        self.idPersona = id  
    
    def nombre(self, nombre: str) -> None:
        # Asigna el nombre a la persona
        self.nombre = nombre
    
    def email(self, correo: str) -> None:
        # Asigna el correo a la persona
        self.email = correo
    
    # GETTERS (
    def obtener_id(self) -> int:
        return self.idPersona  
    
    def obtener_nombre(self) -> str:
        return self.nombre
    
    def obtener_email(self) -> str:
        return self.email
    
    # Metodo para mostarr información
    def mostrarInfo(self):  
        print(f"ID: {self.idPersona} | Nombre: {self.nombre} | Email: {self.email}")