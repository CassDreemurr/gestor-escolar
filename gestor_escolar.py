# Gestor escolar para crear la matrícula del estudiante, almacenar el valor total de sus calificaciones y obtener su promedio.

#Librerias adicionales de python para mejorar el código y la salida de la consola.
from os import system
import random

#Creamos la clase estudiante y sus atributos
class Estudiante:

    def __init__(self, nombre, apellido):
        self.nombre = nombre.capitalize()
        self.apellido = apellido.capitalize()
        self.matricula = 'OWL' + str(random.randrange(100, 200))
        self.calificaciones = []

    # Agregar calificación a la lista
    def agregar_calificacion(self, nota):
        self.calificaciones.append(nota)

    # Calcular promedio
    def calcular_promedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return round(sum(self.calificaciones) / len(self.calificaciones), 1)

    # Mostrar calificaciones
    def mostrar_calificaciones(self):
        system('clear')
        if not self.calificaciones:
            print("Este alumno no tiene calificaciones registradas.\n")
        else:
            print("\nLista de calificaciones:")
            for i, nota in enumerate(self.calificaciones, start=1):
                print(f"Calificación {i}: {nota}")
        input('Presione ENTER para continuar...')
        system('clear')

    # Metodo especial de string para mostrar información del objeto
    def __str__(self):
        return (f"\nEstudiante: {self.nombre} {self.apellido}"
                f"\nMatrícula: {self.matricula}"
                f"\nPromedio actual: {self.calcular_promedio()}\n")


# Función para crear estudiante y devolverlo como tipo objeto
def crear_estudiante():
    system('clear')
    print("Ingrese los datos del estudiante:\n")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    system('clear')
    return Estudiante(nombre, apellido)


# Programa principal
def main():

    # Se crea al estudiante
    estudiante = crear_estudiante()

    menu = """
Menú de opciones
1. Información del estudiante
2. Agregar calificación
3. Mostrar calificaciones
4. Calcular promedio
5. Cerrar programa
"""

    # Empieza el loop de inicio
    while True:
        print(menu)

        # pedir una opción válida al usuario
        try:
            eleccion = int(input("Elija una opción (1-5): "))
        except ValueError:
            print("Entrada inválida.\n")
            input('Presione ENTER para continuar...')
            system('clear')
            continue

        # Se muestra la información del estudiante
        if eleccion == 1:
            system('clear')
            print(estudiante)
            input('Presione ENTER para continuar...')
            system('clear')

        # Se añade una nota a la lista de calificaciones si esta es válida
        elif eleccion == 2:
            system('clear')
            try:
                nota = float(input("Ingrese la calificación: "))
                estudiante.agregar_calificacion(round(nota, 1))
                print("Calificación agregada.\n")
            except ValueError:
                system('clear')
                print("Debe ingresar un número válido.\n")


        # Se muestra la lista de elementos en calificaciones
        elif eleccion == 3:
            estudiante.mostrar_calificaciones()

        # Se calcula el promedio
        elif eleccion == 4:
            system('clear')
            promedio = estudiante.calcular_promedio()
            print(f"Promedio actual: {promedio}\n")
            input('Presione ENTER para continuar...')
            system('clear')

        # Se cancela el loop que ejecuta el programa y este termina
        elif eleccion == 5:
            system('clear')
            print("Programa cerrado.")
            break

        # Mensaje de error si "eleccion" tiene un valor no esperado
        else:
            system('clear')
            print("Opción inválida.\n")


#Ejecutamos el programa principal
main()
