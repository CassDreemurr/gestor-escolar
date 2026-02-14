"""
Gestor Escolar

Este programa permite crear la matrícula de un estudiante,
registrar sus calificaciones y calcular su promedio.
Incluye un menú interactivo en consola para gestionar la información.
"""

# Librerías adicionales para limpiar la consola y generar matrículas aleatorias
from os import system
import random


class Estudiante:
    """
    Clase que representa a un estudiante dentro del sistema escolar.

    Permite:
    - Almacenar nombre y apellido.
    - Generar una matrícula automática.
    - Registrar calificaciones.
    - Calcular el promedio.
    """

    def __init__(self, nombre, apellido):
        """
        Constructor de la clase Estudiante.

        Parámetros:
        nombre (str): Nombre del estudiante.
        apellido (str): Apellido del estudiante.
        """
        self.nombre = nombre.capitalize()
        self.apellido = apellido.capitalize()
        self.matricula = 'OWL' + str(random.randrange(100, 200))
        self.calificaciones = []

    def agregar_calificacion(self, nota):
        """
        Agrega una nueva calificación a la lista del estudiante.

        Parámetros:
        nota (float): Calificación que se desea registrar.
        """
        self.calificaciones.append(nota)

    def calcular_promedio(self):
        """
        Calcula y devuelve el promedio de las calificaciones registradas.

        Retorna:
        float: Promedio redondeado a un decimal.
               Si no hay calificaciones, devuelve 0.
        """
        if len(self.calificaciones) == 0:
            return 0
        return round(sum(self.calificaciones) / len(self.calificaciones), 1)

    def mostrar_calificaciones(self):
        """
        Muestra en pantalla todas las calificaciones registradas
        del estudiante.
        """
        system('clear')
        if not self.calificaciones:
            print("Este alumno no tiene calificaciones registradas.\n")
        else:
            print("\nLista de calificaciones:")
            for i, nota in enumerate(self.calificaciones, start=1):
                print(f"Calificación {i}: {nota}")
        input('Presione ENTER para continuar...')
        system('clear')

    def __str__(self):
        """
        Método especial que define cómo se muestra el objeto
        cuando se imprime en pantalla.
        """
        return (f"\nEstudiante: {self.nombre} {self.apellido}"
                f"\nMatrícula: {self.matricula}"
                f"\nPromedio actual: {self.calcular_promedio()}\n")


def crear_estudiante():
    """
    Solicita al usuario los datos personales y crea
    un objeto de tipo Estudiante.

    Retorna:
    Estudiante: Objeto creado con los datos ingresados.
    """
    system('clear')
    print("Ingrese los datos del estudiante:\n")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    system('clear')
    return Estudiante(nombre, apellido)


def main():
    """
    Función principal que controla el flujo del programa.

    Muestra un menú interactivo que permite:
    - Consultar información del estudiante.
    - Agregar calificaciones.
    - Mostrar calificaciones.
    - Calcular promedio.
    - Salir del programa.
    """

    # Se crea el estudiante al iniciar el programa
    estudiante = crear_estudiante()

    menu = """
Menú de opciones
1. Información del estudiante
2. Agregar calificación
3. Mostrar calificaciones
4. Calcular promedio
5. Cerrar programa
"""

    # Bucle principal del programa
    while True:
        print(menu)

        # Validación de entrada del usuario
        try:
            eleccion = int(input("Elija una opción (1-5): "))
        except ValueError:
            print("Entrada inválida.\n")
            input('Presione ENTER para continuar...')
            system('clear')
            continue

        # Opción 1: Mostrar información del estudiante
        if eleccion == 1:
            system('clear')
            print(estudiante)
            input('Presione ENTER para continuar...')
            system('clear')

        # Opción 2: Agregar una nueva calificación
        elif eleccion == 2:
            system('clear')
            try:
                nota = float(input("Ingrese la calificación: "))
                estudiante.agregar_calificacion(round(nota, 1))
                print("Calificación agregada.\n")
            except ValueError:
                print("Debe ingresar un número válido.\n")

        # Opción 3: Mostrar lista de calificaciones
        elif eleccion == 3:
            estudiante.mostrar_calificaciones()

        # Opción 4: Mostrar promedio actual
        elif eleccion == 4:
            system('clear')
            promedio = estudiante.calcular_promedio()
            print(f"Promedio actual: {promedio}\n")
            input('Presione ENTER para continuar...')
            system('clear')

        # Opción 5: Finalizar programa
        elif eleccion == 5:
            system('clear')
            print("Programa cerrado.")
            break

        # Control de opciones inválidas
        else:
            system('clear')
            print("Opción inválida.\n")


# Punto de entrada del programa
main()

