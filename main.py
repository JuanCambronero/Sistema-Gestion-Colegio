from Colegio import Colegio
from Alumno import Alumno
from Profesor import Profesor
from ClaseGrupo import ClaseGrupo
from Asignatura import Asignatura

def menuAlumno(colegio):
    while True:
        print("\n=== MENU ALUMNOS ===")
        print("="*30)
        print("1. Añadir nuevo alumno")
        print("2. Buscar alumno por ID")
        print("3. Eliminar alumno")
        print("4. Listar todos los alumnos")
        print("0. Volver al menú principal")

        opcion = int(input("Selecciones una opción: "))
        match opcion:
            case 1:
                print("===Añadir Alumno===")
                id_alumno = int(input("ID del alumno: "))
                nombre = input("Nombre completo: ")
                email = input("Email: ")
                grupo = input("Grupo/Curso (ej: 2DAM): ")
                alumno = Alumno(id_alumno,nombre,email,grupo)
                Colegio.addAlumno(colegio,alumno)
            case 2: 
                print("===Buscar Alumnos===")
                id_buscar = int(input("ID del alumno: "))
                Colegio.buscarAlumno(colegio,id_buscar)
            case 3:
                print("===Eliminar Alumnos===")
                id_buscar = int(input("ID del alumno: "))
                Colegio.buscarAlumno(colegio,id_buscar)
                print("Ha sido eliminado correctamente")
                Colegio.eliminarAlumno(colegio,id_buscar)
            case 4:
                print("===Lista de Alumnos===")
                Colegio.listarAlumnos(colegio)
            case 0 :
                break
            case _:
                print("Selecione una opción valida porfavor")


def menuProfesor(colegio):
    while True:
        print("\n=== MENU PROFESORES ===")
        print("="*30)
        print("1. Añadir nuevo profesor")
        print("2. Buscar profesor por ID")
        print("3. Eliminar profesor")
        print("4. Listar todos los profesores")
        print("0. Volver al menú principal")

        opcion = int(input("Selecciones una opción: "))
        match opcion:
            case 1:
                print("===Añadir Profesor===")
                id_profe = int(input("ID del profesor: "))
                nombre = input("Nombre completo: ")
                email = input("Email: ")
                depatamento = input("Departamento: ")
                profesor = Profesor(id_profe,nombre,email,depatamento)
                Colegio.addProfesor(colegio, profesor)
            case 2: 
                print("===Buscar Profesor===")
                id_buscar = int(input("ID del profesor: "))
                Colegio.buscarProfesor(colegio,id_buscar)
            case 3:
                print("===Eliminar Profesor===")
                id_buscar = int(input("ID del profesor: "))
                Colegio.buscarProfesor(colegio,id_buscar)
                print("Ha sido eliminado correctamente")
                Colegio.eliminarProfesor(colegio,id_buscar)
            case 4:
                print("===Lista de Profesores===")
                Colegio.listarProfesores(colegio)
            case 0 :
                break
            case _:
                print("Selecione una opción valida porfavor")





colegio = Colegio("Litterator")
while True:
    print("\n=== SISTEMA GESTIÓN COLEGIO ===")
    print("1. Alumnos")         
    print("2. Profesores") 
    print("3. Grupos")
    print("4. Asignaturas")
    print("5. Listado general")
    print("0. Salir")

    opcion = int(input("Selecciones una opción: "))

    match opcion:
        case 1:
            menuAlumno(colegio)
        case 2: 
            menuProfesor(colegio)
        case 3:
            print("Grupos")
        case 4:
            print("Asignaturas")
        case 5:
            print("Listado General")
        case 0 :
            print("Saliendo...")

