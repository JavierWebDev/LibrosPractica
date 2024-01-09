import os
import func.corefile as cf

libros = {}

cf.MY_DATABASE='data/libros.json'

def NewBook(libro:dict): # Se establece el elemento a añadir
    libros.update(libro) # se añade el elemento al diccionario backup
    cf.AddData(libro) # Se añade al JSON


