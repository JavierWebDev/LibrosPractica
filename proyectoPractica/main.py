'''
Problema de Gestión de Libros en Formato JSON

Escribe un programa en Python para gestionar información de libros mediante un archivo JSON. El programa deberá permitir al usuario realizar las siguientes operaciones:

    Añadir Libro: Añadir un nuevo libro al archivo JSON, especificando título, autor y año de publicación.

    Borrar Libro: Eliminar un libro existente del archivo JSON, proporcionando el título del libro a eliminar.

    Editar Libro: Modificar la información de un libro existente en el archivo JSON. El usuario debe especificar el título del libro a editar, así como los nuevos valores para título, autor y año.

    Buscar Libro: Buscar un libro por su título en el archivo JSON y mostrar su información, si está presente.

Asegúrate de manejar adecuadamente situaciones como la inexistencia de libros en el archivo y proporcionar mensajes informativos al realizar las operaciones. Utiliza funciones para modularizar 
el código y utiliza un archivo JSON llamado 'libros.json' para almacenar la información.
'''
import os
import ui.mainMenu as mainmenu
import ui.menuLibros as mLibro

libros = {}

def main():
    isActiveApp = True

    while isActiveApp:
        op = mainmenu.mainMenu()
        if op == 1:
            mLibro.generarLibroMenu(libros)
        elif op == 2:
            mLibro.editLibro()
        elif op == 3:
            mLibro.delLibro(libros)
        elif op == 4:
            mLibro.mostrarLibro()




if __name__ == '__main__':
    main()