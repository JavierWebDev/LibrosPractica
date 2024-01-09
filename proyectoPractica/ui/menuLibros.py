import os
import func.libros as lb

libros = {}

def generarLibroMenu():
    isActiveRegLibro = True
    header = '''
    ***********************
    *   REGISTRAR LIBRO   *
    ***********************
    '''
    while isActiveRegLibro:
        print(header)
        
        try: 
            nombre = str(input("[-] Ingresa titulo del libro: "))
            autor = str(input(f"[-] Ingresa autor del libro ({nombre}): "))
            anioPublicacion = str(input(f"[-] Ingresa año de publicacion del libro ({nombre}): "))
        except ValueError:
            print("\033[91m[!] VALOR ERRONEO\033[0m")
            os.system("pause")
        else:
            libro = {
                'ID':'',
                'nombre':nombre,
                'autor':autor,
                'fechaPublicacion':anioPublicacion
            }
            libros.update({libro})

