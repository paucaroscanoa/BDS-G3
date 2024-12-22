#tuplas : igual a las listas pero inmutables
dias=('lunes','martes','miercoles','jueves')
print(dias)
print(type(dias))
# Para agregar datos convertirmos la tupla en lista
dias=list(dias)
print(type(dias))
dias.append("viernes")
dias=tuple(dias)
print(type(dias))


#recorrer una lista
for dia in dias:
    print(dia)