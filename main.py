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

def menuGrupo (colegio):
    while True:
        print("\n=== MENU CLASES ===")
        print("="*30)
        print("1. Crear nueva clase")
        print("2. Buscar clase")
        print("3. Asignar tutor")
        print("4. Añadir alumnos")
        print("5. Lista de clase")
        print("6. Mostrar Clase")
        print("0. Volver al menú principal")

        opcion = int(input("Selecciones una opción: "))
        match opcion:
            case 1:
                print("===Crear Clase===")
                id_clase = int(input("ID de la clase: "))
                nombre = input("Nombre de la clase: ")
                clase_grupo = ClaseGrupo(id_clase, nombre)
                Colegio.addClaseGrupo(colegio, clase_grupo)
                
            case 2: 
                print("===Buscar Clase===")
                id_buscar = int(input("ID de la clase: "))
                clase = Colegio.buscarClase(colegio, id_buscar)
                if clase:
                    print(clase.mostarInfo())
                else:
                    print("Clase NO encontrada")
            case 3:
                print("===Asignar Tutor===")
                id_clase = int(input("ID de la clase: "))
                clase = Colegio.buscarClase(colegio, id_clase)
                if clase:
                    id_profesor = int(input("ID del profesor tutor: "))
                    profesor = colegio.profesores.get(id_profesor)
                    if profesor:
                        clase.asignarTutor(profesor)
                        print("Tutor asignado correctamente")
                    else:
                        print("Profesor NO encontrado")
                else:
                    print("Clase NO encontrada")
            case 4:
                print("===Añadir Alumno al Grupo===")
                id_clase = int(input("ID de la clase: "))
                clase = Colegio.buscarClase(colegio, id_clase)
                if clase:
                    id_alumno = int(input("ID del alumno: "))
                    alumno = colegio.alumnos.get(id_alumno)
                    if alumno:
                        clase.addAlumno(alumno)
                        print("Alumno añadido correctamente")
                    else:
                        print("Alumno NO encontrado")
                else:
                    print("Clase NO encontrada")
            case 5:
                print("===Listar Grupos===")
                if colegio.clases:
                    for clase in colegio.clases:
                        print(clase.mostarInfo())
                else:
                    print("No hay grupos registrados")
            case 6:
                print("===Datos Completos del Grupo===")
                id_buscar = int(input("ID de la clase: "))
                clase = Colegio.buscarClase(colegio, id_buscar)
                if clase:
                    print(f"\n{'='*50}")
                    print(f"GRUPO: {clase.nombre} (ID: {clase.id})")
                    print(f"{'='*50}")
                    
                    # Mostrar datos del tutor
                    if clase.tutor:
                        print(f"\nTUTOR:")
                        print(f"  {clase.tutor.mostrarInfo()}")
                    else:
                        print(f"\nTUTOR: Sin asignar")
                    
                    # Mostrar datos de los alumnos
                    print(f"\nALUMNOS ({len(clase.alumnos)}):")
                    if clase.alumnos:
                        for i, alumno in enumerate(clase.alumnos, 1):
                            print(f"  {i}. {alumno.mostrarInfo()}")
                    else:
                        print("  No hay alumnos en este grupo")
                    print(f"{'='*50}\n")
                else:
                    print("Clase NO encontrada")
            case 0 :
                break
            case _:
                print("Selecione una opción valida porfavor")


def menuAsignatura(colegio):
    while True:
        print("\n=== MENU ASIGNATURAS ===")
        print("="*30)
        print("1. Crear nueva asignatura")
        print("2. Buscar asignatura por ID")
        print("3. Asignar profesor a asignatura")
        print("4. Inscribir alumno en asignatura")
        print("5. Listar todas las asignaturas")
        print("6. Mostrar datos completos de asignatura")
        print("7. Eliminar asignatura")
        print("8. Asignar nota a alumno")
        print("9. Ver notas de una asignatura")
        print("10. Ver nota de un alumno específico")
        print("0. Volver al menú principal")

        opcion = int(input("Selecciones una opción: "))
        match opcion:
            case 1:
                print("===Crear Asignatura===")
                id_asig = int(input("ID de la asignatura: "))
                nombre = input("Nombre de la asignatura: ")
                asignatura = Asignatura(id_asig, nombre)
                Colegio.addAsignatura(colegio, asignatura)
                print("Asignatura creada correctamente")
                
            case 2:
                print("===Buscar Asignatura===")
                id_buscar = int(input("ID de la asignatura: "))
                asignatura = Colegio.buscarAsignatura(colegio, id_buscar)
                if asignatura:
                    print(asignatura.mostrarInfo())
                else:
                    print("Asignatura NO encontrada")
                    
            case 3:
                print("===Asignar Profesor===")
                id_asig = int(input("ID de la asignatura: "))
                asignatura = Colegio.buscarAsignatura(colegio, id_asig)
                if asignatura:
                    id_profesor = int(input("ID del profesor: "))
                    profesor = colegio.profesores.get(id_profesor)
                    if profesor:
                        asignatura.asignar_profesor(id_profesor)
                        profesor.addAsignatura(id_asig)
                        print("Profesor asignado correctamente")
                    else:
                        print("Profesor NO encontrado")
                else:
                    print("Asignatura NO encontrada")
                    
            case 4:
                print("===Inscribir Alumno===")
                id_asig = int(input("ID de la asignatura: "))
                asignatura = Colegio.buscarAsignatura(colegio, id_asig)
                if asignatura:
                    id_alumno = int(input("ID del alumno: "))
                    alumno = colegio.alumnos.get(id_alumno)
                    if alumno:
                        asignatura.inscribir_alumno(id_alumno)
                        print("Alumno inscrito correctamente")
                    else:
                        print("Alumno NO encontrado")
                else:
                    print("Asignatura NO encontrada")
                    
            case 5:
                print("===Lista de Asignaturas===")
                if colegio.asignatura:
                    Colegio.listarAsignaturas(colegio)
                else:
                    print("No hay asignaturas registradas")
                    
            case 6:
                print("===Datos Completos de la Asignatura===")
                id_buscar = int(input("ID de la asignatura: "))
                asignatura = Colegio.buscarAsignatura(colegio, id_buscar)
                if asignatura:
                    print(f"ASIGNATURA: {asignatura.nombre} (ID: {asignatura.id})")
                    print(f"{'='*50}")
                    
                    # Mostrar datos del profesor
                    if asignatura.profesor_id:
                        profesor = colegio.profesores.get(asignatura.profesor_id)
                        if profesor:
                            print(f"PROFESOR:")
                            print(f"{profesor.mostrarInfo()}")
                    else:
                        print(f"PROFESOR: Sin asignar")
                    
                    # Mostrar datos de los alumnos inscritos
                    print(f"\nALUMNOS INSCRITOS ({len(asignatura.alumnos)}):")
                    if asignatura.alumnos:
                        for i, alumno_id in enumerate(asignatura.alumnos, 1):
                            alumno = colegio.alumnos.get(alumno_id)
                            if alumno:
                                print(f"  {i}. {alumno.mostrarInfo()}")
                    else:
                        print("No hay alumnos inscritos")
                else:
                    print("Asignatura NO encontrada")
            case 7:
                print("===Eliminar Asignatura===")
                id_buscar = int(input("ID de la asignatura: "))
                asignatura = Colegio.buscarAsignatura(colegio, id_buscar)
                if asignatura:
                    print(asignatura.mostrarInfo())
                    Colegio.eliminarAsignatura(colegio, id_buscar)
                    print("Asignatura eliminada correctamente")
                else:
                    print("Asignatura NO encontrada")
            case 8:
                print("===Asignar Nota a Alumno===")
                id_asig = int(input("ID de la asignatura: "))
                asignatura = Colegio.buscarAsignatura(colegio, id_asig)
                if asignatura:
                    id_alumno = int(input("ID del alumno: "))
                    if id_alumno in asignatura.alumnos:
                        nota = float(input("Nota (0-10): "))
                        if 0 <= nota <= 10:
                            asignatura.asignar_nota(id_alumno, nota)
                            print("Nota asignada correctamente")
                        else:
                            print("La nota debe estar entre 0 y 10")
                    else:
                        print("El alumno no está inscrito en esta asignatura")
                else:
                    print("Asignatura NO encontrada")
                    
            case 9:
                print("===Ver Notas de la Asignatura===")
                id_asig = int(input("ID de la asignatura: "))
                asignatura = Colegio.buscarAsignatura(colegio, id_asig)
                if asignatura:
                    print(f"\nNotas de {asignatura.nombre}:")
                    for alumno_id in asignatura.alumnos:
                        alumno = colegio.alumnos.get(alumno_id)
                        nota = asignatura.obtener_nota(alumno_id)
                        
                        nombre = alumno.nombre if alumno else f"ID {alumno_id}"
                        print(f"  {nombre} - {nota}")
                else:
                    print("Asignatura NO encontrada")
                    
            case 10:
                print("===Ver Notas del Alumno===")
                id_alumno = int(input("ID del alumno: "))
                alumno = colegio.alumnos.get(id_alumno)
                if alumno:
                    print(f"\nNotas de {alumno.nombre}:")
                    for id_asig, asignatura in colegio.asignatura.items():
                        if id_alumno in asignatura.alumnos:
                            nota = asignatura.obtener_nota(id_alumno)
                            
                            print(f"  {asignatura.nombre} - {nota}")
                else:
                    print("Alumno NO encontrado")
            case 0:
                break
            case _:
                print("Selecione una opción valida porfavor")


colegio = Colegio("Litterator")
# Datos de ejemplo
# Crear profesores
prof1 = Profesor(1, "María García", "maria.garcia@colegio.es", "Matemáticas")
prof2 = Profesor(2, "Juan Pérez", "juan.perez@colegio.es", "Informática")
prof3 = Profesor(3, "Ana Martínez", "ana.martinez@colegio.es", "Lengua")
Colegio.addProfesor(colegio, prof1)
Colegio.addProfesor(colegio, prof2)
Colegio.addProfesor(colegio, prof3)

# Crear alumnos
alumno1 = Alumno(101, "Carlos López", "carlos.lopez@estudiante.es", "2DAM")
alumno2 = Alumno(102, "Laura Sánchez", "laura.sanchez@estudiante.es", "2DAM")
alumno3 = Alumno(103, "Pedro Ruiz", "pedro.ruiz@estudiante.es", "2DAM")
alumno4 = Alumno(104, "Sofía Moreno", "sofia.moreno@estudiante.es", "1DAM")
alumno5 = Alumno(105, "Diego Fernández", "diego.fernandez@estudiante.es", "1DAM")
Colegio.addAlumno(colegio, alumno1)
Colegio.addAlumno(colegio, alumno2)
Colegio.addAlumno(colegio, alumno3)
Colegio.addAlumno(colegio, alumno4)
Colegio.addAlumno(colegio, alumno5)

# Crear grupos
grupo1 = ClaseGrupo(1, "2DAM", prof2)
grupo1.addAlumno(alumno1)
grupo1.addAlumno(alumno2)
grupo1.addAlumno(alumno3)
Colegio.addClaseGrupo(colegio, grupo1)

grupo2 = ClaseGrupo(2, "1DAM", prof1)
grupo2.addAlumno(alumno4)
grupo2.addAlumno(alumno5)
Colegio.addClaseGrupo(colegio, grupo2)

# Crear asignaturas
asig1 = Asignatura(1, "Programación")
asig1.asignar_profesor(2)
asig1.inscribir_alumno(101)
asig1.inscribir_alumno(102)
asig1.inscribir_alumno(103)
prof2.addAsignatura(1)
Colegio.addAsignatura(colegio, asig1)

asig2 = Asignatura(2, "Bases de Datos")
asig2.asignar_profesor(2)
asig2.inscribir_alumno(101)
asig2.inscribir_alumno(102)
prof2.addAsignatura(2)
Colegio.addAsignatura(colegio, asig2)

asig3 = Asignatura(3, "Matemáticas")
asig3.asignar_profesor(1)
asig3.inscribir_alumno(104)
asig3.inscribir_alumno(105)
prof1.addAsignatura(3)
Colegio.addAsignatura(colegio, asig3)
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
            menuGrupo(colegio)
        case 4:
            menuAsignatura(colegio)
        case 5:
            print("Listado General")
        case 0 :
            print("Saliendo...")
            break

