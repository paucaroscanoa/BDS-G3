print("Mi Calculadora")
#ENTRADA
n1=input("ingrese nro1 :") #input ingresa el dato como texto
n2=input("ingrese nro2 :")
operacion = input("Que operación desea hacer (suma/resta/multiplicación/división)")

#PROCESO
if(operacion=="suma"): #== doble igual es asignación
    resultado=int(n1)+int(n2)
elif(operacion=="resta"): 
    resultado=int(n1)-int(n2)
elif(operacion=="multiplicación"): 
    resultado=int(n1)*int(n2)
elif(operacion=="división"): 
    resultado=int(n1)/int(n2)
else:
    print("La Operación no existe!!!")
    exit()
#SALIDA
print (f"la {operacion} de {n1} y {n2} es {resultado}")