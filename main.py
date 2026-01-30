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
                print(Colegio.buscarAlumno(colegio,id_buscar))
            case 3:
                print("Eliminar Alumno")
            case 4:
                print("Mostrar Alumnos")
            case 5:
                print("Volver al menú principal")
            case 0 :
                print("Volviendo")

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
            print("Profesores")
        case 3:
            print("Grupos")
        case 4:
            print("Asignaturas")
        case 5:
            print("Listado General")
        case 0 :
            print("Saliendo...")

