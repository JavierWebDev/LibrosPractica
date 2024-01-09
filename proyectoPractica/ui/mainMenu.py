import os 

opcionesPrincipales = ["Agregar Libros", "Editar Informacion del libro", "Borrar Libros", "Mostrar Libros"]
def mainMenu()->int:
    header = '''
    ************************
    *   GESTOR DE LIBROS   *
    ************************
    '''

    try:
        print(header)
        for i, item in enumerate(opcionesPrincipales):
            print(f"{i+1}. {item}")
        op = int(input(" >) "))
    except ValueError:
        print("\033[91m[!] VALOR ERRONEO\033[0m")
        os.system("pause")
    else:
        return op