#Profesor lo creara sebas

#clase que hereda de la clase persona que es la clase padre

from Personas import Personas

class Profesor(Personas):
    
    #constructor profesor
    def __init__ (self,id_profesor,nombre,departamento):
        
        #constructor de la clase persona, guarda id y nombre
        super().__init__(id_profesor,nombre)
        
        #guardamos el departamento de la asignatura que imparte
        self.departamento=departamento
        
        #creo una lista vacia para las asignaturas que da el profesor
        self.asignaturas=[]
        
        
    #getter para obtener departamentos
        
    def get_departamento(self):
        return self.departamento
    
    
    #geeter para obtener asignaturas
    def get_asignaturas(self):
        return self.asignaturas
        
        

