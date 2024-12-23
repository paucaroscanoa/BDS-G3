import os
from time import sleep
    
"""
    CRUD
    - CREATE
    - READ
    - UPDATE
    - DELETE

"""
dic_alumnos={
        '12345678':{
            'nombre':'CESAR',
            'email':'cesar@gmail.com'
    }
}
    
ANCHO =50
opcion=0
    
while(opcion<5):
    os.system("clear")   
    print("="*ANCHO)
    print(" "*10 + "GESTION DE ALUMNOS")
    print("="*ANCHO)
    print("""
         [1] REGISTRAR ALUMNO
         [2] MOSTRAR ALUMNOS
         [3] ACTUALIZAR ALUMNO
         [4] ELIMINAR ALUMNO
         [5] SALIR
              """)
    print("="*ANCHO)
    
opciOn =int(input("INGRESE OPCIÓN : "))
os.system("clear")     
   
if opciOn ==1:
    print("="*ANCHO)
    print(" "*10 + "[1] INGRSAR ALUMNO")
    print("="*ANCHO)
    dni = input("DNI   :")
    nombre = input("NOMBRE    :")
    email =input("EMAIL    :")
    dic_nuevo_alumno ={
        'nombre':nombre,
        'email': email
    }
    dic_alumnos.update(dic_nuevo_alumno) 
elif opciOn ==2:
    print("="*ANCHO)
    print(" "*10 + "[2] MOSTRAR ALUMNOS")
    print("="*ANCHO)
    for dni,datos in dic_alumnos.items():
        print(f"DNI:{datos['dni']}")
        print(f"Nombre:{datos['nombre']}")
        print(f"EMAIL:{datos['email']}")
        print("*"*ANCHO)    
        input("Presiones ENTER para continuar ...")
elif opciOn ==3:
    print("="*ANCHO)
    print(" "*10 + "[3] ACTUALIZAR ALUMNO")
    print("="*ANCHO)
    if dni in dic_alumnos:
        print(f"ALUMNO A ACTUALIZAR {dic_alumnos[dni]['nombre']}")
elif opciOn ==4:
    print("="*ANCHO)
    print(" "*10 + "[4] ELIMINAR ALUMNO")
    print("="*ANCHO)
elif opciOn ==5:
    print("="*ANCHO)
    print(" "*10 + "[5] SALIR")
    print("="*ANCHO)
else:
    print("="*ANCHO)
    print(" "*10 + "OPCIÓN INVALIDA")
    print("="*ANCHO)
                   
sleep(1)
#minuto 2:17 0408