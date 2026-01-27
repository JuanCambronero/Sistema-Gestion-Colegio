import Personas
import Colegio
import Alumno
import Profesor


colegio = Colegio.Colegio("Colegio Litterator")

# Crear Alumnos y Profesores
al1 = Alumno.Alumno(1, "Juan", "Juan@gmail.com", "2ªDAM")
al2 = Alumno.Alumno(2, "Sebas", "Sebas@gmail.com", "2ºDAM")
pr1 = Profesor.Profesor(3, "Hector", "Tecnologia")
    
pasua = input("Pulse algo para seguir")
#AÑADIR
print("TEST 1: AÑADIR")
colegio.addAlumno(al1)
colegio.addProfesor(pr1)
colegio.addAlumno(al2)

pasua = input("Pulse algo para seguir")
#BUSCAR
print("\nTEST 2: BUSCAR")
colegio.buscarAlumno(1)
pasua = input("Pulse algo para seguir")


#ELIMINAR
print("\nTEST 3: ELIMINAR")
colegio.eliminarAlumno(2)
colegio.buscarAlumno(2) #Aqui si esta bien echo peta


