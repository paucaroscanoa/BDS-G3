# def : define la función y esta puede ser utlizado en cualquier parte del programa
# suma simple
def sumar(n1,n2):
    resultado =n1+n2
    return resultado

n1 = input("ingrese nro 1 :")
n2 = input("ingrese nro 2 :")
suma =sumar(int(n1), int(n2))
print(f'la suma de {n1}+{n2} es {suma}')

# suma con mensaje
def sumarmsj(n1,n2):
    resultado =n1+n2
    return resultado
def sumar_con_mensaje(n1,n2):
    resultado = int(n1)+int(n2)
    print(f'SUMA CON MENSAJE : la suma de {n1}+{n2} es {resultado}')
    
n1 = input("ingresemsj nro 1 :")
n2 = input("ingresemsj nro 2 :")
suma =sumarmsj(int(n1), int(n2))
print(f'la suma de {n1}+{n2} es {suma}')
sumar_con_mensaje(n1,n2)

