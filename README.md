<div align="center">
  
#  Sistema Gestión Colegio - Práctica POO Python 

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Stable-success?style=for-the-badge)



</div>


##  Descripción

Sistema de gestión escolar completo desarrollado como práctica de **Programación Orientada a Objetos en Python**. Permite administrar alumnos, profesores, grupos, asignaturas y calificaciones a través de una interfaz de consola interactiva.

##  Características Principales

####  Gestión de Alumnos
- ➕ Añadir nuevos alumnos
- 🔍 Buscar alumnos por ID
- 🗑️ Eliminar alumnos
- 📋 Listar todos los alumnos
- 📊 Ver expediente completo con notas

####  Gestión de Profesores
- ➕ Añadir nuevos profesores
- 🔍 Buscar profesores por ID
- 🗑️ Eliminar profesores
- 📋 Listar todos los profesores
- 📚 Asignar asignaturas a profesores

####  Gestión de Grupos/Clases
- ➕ Crear nuevos grupos
- 🔍 Buscar grupos por ID
- 👤 Asignar tutor a grupo
- 👥 Añadir alumnos a grupos
- 📋 Listar todos los grupos
- 📊 Ver datos completos (tutor + alumnos)

####  Gestión de Asignaturas
- ➕ Crear nuevas asignaturas
- 🔍 Buscar asignaturas por ID
- 👨‍🏫 Asignar profesor
- 👥 Inscribir alumnos
- 📋 Listar todas las asignaturas
- 📊 Ver datos completos (profesor + alumnos)
- 🗑️ Eliminar asignaturas

####  Gestión de Notas
- ✍️ Asignar notas (0-10) a alumnos
- 📊 Ver todas las notas de una asignatura
- 🎓 Ver expediente completo de un alumno
- 📈 Validación automática de rangos

---

## Ramas del Proyecto
| Rama    | Estado        | Descripción       |
| ------- | ------------- | ----------------- |
| main    |  Estable      | Codigo funcional |
| desarrollo |  En progreso | Experimentos      |
## Diagrama UML
![Diagrama_UML_Gestion_Colegio_Detallado_page-0001](https://github.com/user-attachments/assets/e87dcae9-92b9-4b11-953d-d7c56eb3e36c)



## Casos de uso

### Datos de Prueba Precargados

El sistema incluye datos de ejemplo que se cargan automáticamente:

| Tipo | Cantidad | Detalles |
|------|----------|----------|
| 👨‍🏫 **Profesores** | 3 | María García, Juan Pérez, Ana Martínez |
| 👥 **Alumnos** | 5 | Carlos, Laura, Pedro, Sofía, Diego |
| 🏫 **Grupos** | 2 | 1DAM, 2DAM (con tutores asignados) |
| 📚 **Asignaturas** | 3 | Programación, Bases de Datos, Matemáticas |

### Navegación por Menús

```
=== SISTEMA GESTIÓN COLEGIO ===
1. Alumnos         → Gestión completa de estudiantes
2. Profesores      → Gestión completa de docentes
3. Grupos          → Gestión de clases y tutorías
4. Asignaturas     → Gestión de materias y notas
5. Listado general → Vista general del sistema
0. Salir           → Cerrar el programa
```

### Ejemplos de Uso Rápido

#### 📝 Asignar una Nota
1. Menú Principal → `4` (Asignaturas)
2. Menú Asignaturas → `8` (Asignar nota a alumno)
3. Ingresar ID de asignatura: `1`
4. Ingresar ID de alumno: `101`
5. Ingresar nota: `8.5`

#### 👀 Ver Expediente de Alumno
1. Menú Principal → `4` (Asignaturas)
2. Menú Asignaturas → `10` (Ver notas del alumno)
3. Ingresar ID de alumno: `101`

#### 🏫 Ver Información de Grupo
1. Menú Principal → `3` (Grupos)
2. Menú Grupos → `6` (Mostrar datos completos)
3. Ingresar ID de clase: `1`

## Memoria del proyecto

[Memoria_trabajo_Poo_Grupo_Finalizado.pdf](https://github.com/user-attachments/files/25005613/Memoria_trabajo_Poo_Grupo_Finalizado.pdf)



## Instalación

### Requisitos Previos
- Python 3.10 o superior

### Pasos de Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/sistema-gestion-colegio.git
cd sistema-gestion-colegio

# 2. Ejecutar el programa
python main.py
```

---

