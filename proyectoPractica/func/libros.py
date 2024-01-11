import os
import func.corefile as cf

libros = {}

cf.MY_DATABASE='data/libros.json'

def NewBook(libro:dict): # Se establece el elemento a añadir
    libros.update(libro) # se añade el elemento al diccionario backup
    cf.AddData(libro) # Se añade al JSON

def Searchbook()->dict:
    id=input('Ingrese el Nro Id :')
    return libros.get(id)

def DelBook(libros:dict, id:str):
    libros.pop(libros[id])
    cf.delData(libros, id)

def EditBook(key:str, libro:dict):
    for key in libro.items():
        if key in libros.items():
            if key != 'ID':
                if bool(input(f"[?] Desea editar el campo {key}? (ENTER - SI | Ingresa un digito - NO) \n >) ")):
                    libro[key] = input(f"[-] Ingrese el {key.capitalize()} del libro: ")
        libros[key].update(libro)
        cf.NewFile(libros)
    