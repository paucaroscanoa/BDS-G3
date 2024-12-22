#Programa para convertir monedas de soles a dólares y de dolares a soles
import os
from time import sleep

#ENTRADA
TIPO_CAMBIO_COMPRA=3.7
TIPO_CAMBIO_VENTA=3.8
bandera = True
#PROCESO
while (bandera):
    print("""
          ================================
                CONVERTIDOR DE MONEDAS
          ================================
          [1] CONVERTIR DE SOLES A DOLARES
          [2] CONVERTIR DE DOLARES A SOLES 
          [3] SALIR
          """)
    opción = int(input("ELIJA LA OPCIÓN: "))
    os.system("clear")
    if(opción==1):
        print("""
            =================================
                CONVIRTIENDO SOLES A DOLARES
            =================================""")
        monto_origen=float(input("INGRESE MONTO EN SOLES :"))
        monto_destino= monto_origen/TIPO_CAMBIO_VENTA
        print(f"EL MONTO EN DOLARES ES{monto_destino}")
    elif(opción==2):
        print("""=============================
                 CONVERTIENDO DOLARES A SOLES
                 =============================""")
        monto_origen=float(input("INGRESE MONTO EN DOLARES : "))
        monto_destino = monto_origen*TIPO_CAMBIO_COMPRA
        print(f"EL MONTO EN SOLES ES{monto_destino}")
    elif(opción==3):
        bandera = False
        print("""=============================
                     SALIENDO DE PROGRAMA
                 =============================""")
    else:
        print("OPCIÓN VÁLIDA!!!!")
        break
    sleep(5)
    os.system("clear")
    
#SALIDA 