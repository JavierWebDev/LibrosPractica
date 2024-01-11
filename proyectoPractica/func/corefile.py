import os
import json

MY_DATABASE=''

def NewFile(*param):
    with open(MY_DATABASE,"w") as wf:
        json.dump(param[0],wf,indent=4)

def AddData(*param):
    # Abre el archivo JSON en modo lectura y escritura ('r+')
    with open(MY_DATABASE, "r+") as rwf:
        # Carga el contenido actual del archivo JSON en un diccionario llamado data_file
        data_file = json.load(rwf)
        
        # Verifica si se proporcionaron más de un parámetro (si es más de un parámetro, entonces se espera una llave y un valor)
        if (len(param) > 1):
            # Actualiza el diccionario data_file con la nueva llave y valor
            data_file.update({param[0]: param[1]})
        else:
            # Si solo se proporciona un parámetro, asume que es un diccionario y lo actualiza en data_file
            data_file.update(param[0])
        
        # Mueve el cursor al inicio del archivo
        rwf.seek(0)
        
        # Escribe el diccionario actualizado (data_file) en el archivo JSON
        json.dump(data_file, rwf, indent=4)
        
        # Cierra el archivo
        rwf.close()

def ReadFile():
    # Abre el archivo JSON en modo lectura ('r')
    with open(MY_DATABASE, "r") as rf:
        # Carga el contenido del archivo JSON en un diccionario y lo devuelve
        return json.load(rf)
    
def checkFile(*param):
    # Convierte los parámetros en una lista llamada 'data'
    data = list(param)
    
    # Verifica si el archivo especificado por la variable 'MY_DATABASE' existe
    if os.path.isfile(MY_DATABASE):
        # Si se proporcionaron parámetros, actualiza el primer parámetro con el contenido del archivo existente
        if len(param):
            data[0].update(ReadFile())
    else:
        # Si se proporcionaron parámetros, crea un nuevo archivo con el primer parámetro
        if len(param):
            NewFile(data[0])

def delData(*param):
    data = list(param)
    data[0].pop(data[1])
    NewFile(data[0])

