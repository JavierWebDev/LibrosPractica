import os
import func.libros as lb
import func.corefile as cf
import json


def generarLibroMenu(libros:dict):
    cf.checkFile(libros)
    isActiveRegLibro = True
    header = '''
    ************************
    *   REGISTRAR LIBROS   *
    ************************
    '''

    rta = "S"
    while rta in ["S","s"]:
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
                'ID': '',
                'nombre': nombre,
                'autor': autor,
                'fechaPublicacion': anioPublicacion
            }
            
            id = (str(len(libros)).zfill(3))
            libro['ID'] = id
            libros.update({libro['ID']: libro})

            lb.NewBook(libros)

            rta = input("[?] ¿Deseas ingresar otro libro? ([S] SI - [N] NO)\n >)")
        


def delLibro(libros: dict):
    isActiveDelLibro = True
    header = '''
    ***********************
    *   ELIMINAR LIBROS   *
    ***********************
    '''
    while isActiveDelLibro:
        try:
            idDel = str(input("Ingresa el ID del libro a eliminar: "))
        except ValueError:
            print("\033[91m[!] VALOR ERRONEO\033[0m")
            os.system("pause")
        else:
            if idDel in libros:
                lb.DelBook(libros, idDel)
                print(f"[+] Libro con ID {idDel} eliminado exitosamente.")
            else:
                print(f"[-] No existe un libro con ID {idDel}.")
            rta = input("[?] ¿Deseas eliminar otro libro? ([S] SI - [N] NO)\n >) ").upper()
            if rta != "S":
                isActiveDelLibro = False

# def editLibro():
#     isActiveEdiLibro = True
#     header = '''
#     *********************
#     *   EDITAR LIBROS   *
#     *********************
#     '''
#     while isActiveEdiLibro:
#         try:
#             os.system("pause")
#             print(header)
#             data = lb.Searchbook()
#         except ValueError:
#             print("\033[91m[!] VALOR ERRONEO\033[0m")
#             os.system("pause")
#         else:
#             print(data)
#             os.system("pause")
#             lb.EditBook(data['ID'],data)
                
def mostrarLibro():
    print(lb.Searchbook())
    os.system("pause")