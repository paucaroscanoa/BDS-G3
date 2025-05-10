bandera="si"
while(bandera=="si"):
    print("_____________CALCULADORA CON PYHTON______________")
    n1=input("ingrese nro1 :") #input ingresa el dato como texto
    n2=input("ingrese nro2 :")
    operacion = int(input("""INGRESE EL TIPO DE OPERACIÓN
                  1) SUMA
                  2) RESTA
                  3) MULTIPLICACIÓN
                  4) DIVISION
                  """))
    if(operacion==1): #== doble igual es asignación
        resultado=int(n1)+int(n2)
        print (f"la {operacion} de {n1} y {n2} es {resultado}")
    elif(operacion==2): 
        resultado=int(n1)-int(n2)
        print (f"la {operacion} de {n1} y {n2} es {resultado}")
    elif(operacion==3): 
        resultado=int(n1)*int(n2)
        print (f"la {operacion} de {n1} y {n2} es {resultado}")
    elif(operacion==4): 
        resultado=int(n1)/int(n2)
        print (f"la {operacion} de {n1} y {n2} es {resultado}")
    else:
        print("La Operación no existe!!!")
    #SALIDA
    bandera =input("¿desea continua ")