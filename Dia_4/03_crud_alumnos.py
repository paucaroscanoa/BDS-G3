import os
from time import sleep
from matricula.lib_alumnos import *
    
"""
    CRUD
    - CREATE
    - READ
    - UPDATE
    - DELETE

"""  
cargar_alumnos('alumnos.txt')
opcion=0

    
while(opcion<5):
    os.system("clear")   
    menu()
    opcion =int(input("INGRESE OPCIÓN : "))
    os.system("clear")     
   
    if opcion ==1:
        dic_nuevo_alumno=registrar()
        dic_alumnos.update(dic_nuevo_alumno) 
    elif opcion ==2:
        mostrar()
        input("Presiona ENTER para continuar ...")
    elif opcion ==3:
        actualizar() 
    elif opcion ==4:
        eliminar()
    elif opcion ==5:
        grabar_alumnos('alumnos.txt')
        mostrar_mensaje("[5] SALIR")
    else:
        mostrar_mensaje("OPCIÓN INVALIDA!!!")
                    
    sleep(1)
