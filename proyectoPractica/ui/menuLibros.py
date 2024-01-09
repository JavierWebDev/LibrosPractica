import os
import func.libros as lb
import func.corefile as cf
import json

libros = {}

def generarLibroMenu(libros:dict):
    cf.checkFile(libros)
    cf.ReadFile()
    isActiveRegLibro = True
    header = '''
    ************************
    *   REGISTRAR LIBROS   *
    ************************
    '''
    isActiveRegLibro = True
    idContador = 0
    while isActiveRegLibro:
        os.system("cls")
        print(header)
        

        try:
            nombre = str(input("[-] Ingresa título del libro: "))
            autor = str(input(f"[-] Ingresa autor del libro ({nombre}): "))
            anioPublicacion = str(input(f"[-] Ingresa año de publicación del libro ({nombre}): "))
        except ValueError:
            print("\033[91m[!] VALOR ERRONEO\033[0m")
            os.system("pause")
        else:
            libro = {
                'ID': idContador + 1,
                'nombre': nombre,
                'autor': autor,
                'fechaPublicacion': anioPublicacion
            }
            
            libros.update({libro['ID']:libro})
            idContador += 1

            lb.NewBook(libros)

            rta = input("[?] ¿Deseas ingresar otro libro? ([S] SI - [N] NO)\n >) ").upper()
            if rta != "S":
                isActiveRegLibro = False

            

