import os
import re

ruta = "/home/cass/Pythoncharm/Dia 9/Instrucciones/Mi_Gran_Directorio"

patron = r'N[a-zA-Z]{3}-\d{5}'


def leer_archivos(rut, archi):
    archivos_encontrados = []
    rutas_encontradas = []
    with open(rut, 'r') as texto:
        contenido = texto.read()

        if re.search(patron, contenido):
            archivos_encontrados.append(archi)
            rutas_encontradas.append(rut)

    return archivos_encontrados,rutas_encontradas

def encontrar_rutas(r):
    ruta_archivo = []
    for carpeta, subcarpeta, archivo in os.walk(r):
        for arch in archivo:
            ruta_archivo = (os.path.join(carpeta, arch))
    return ruta_archivo