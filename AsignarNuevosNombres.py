import os
import re

# Expresiones que se van a usar para cambiar el nombre a archivos
quitarEspacios = r" "
patron = re.compile(r".{1,9}([0-9]|[0-9][0-9]).pdf")
reemplazo = re.compile(r"^[a-zA-Z]{1,9}")

# Preparacion del programa para insertar a la carpeta
directorio = input("Inserta la dirección de la carpeta donde quieres cambiar el nombre")
os.chdir(directorio)
elementos = os.listdir(directorio)

#Cambio de nombre a todos los archivos dentro de toda la carpeta
for archivo in elementos:
    if (patron.match(archivo)):
        print("El archivo",archivo,"cumple")
        #Asignación de nuevo nombre
        nuevoNombre = reemplazo.sub("Clase ", archivo.replace(" ", ""))
        print("El nuevo nombre es:", nuevoNombre)
        os.rename(archivo,nuevoNombre)