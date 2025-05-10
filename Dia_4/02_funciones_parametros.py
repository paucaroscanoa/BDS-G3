#Parametros args y kwargs
def suma_infinito(*args):
    resultado=0
    for numero in args:
        resultado=resultado+numero
    return resultado

suma1=suma_infinito(1,2,3,4)
print(suma1)
suma2=suma_infinito(1,2,3)
print(suma2)

def calculadora(**kwargs):
    ope = kwargs.get('ope')
    n1=kwargs.get('n1')
    n2=kwargs.get('n2')
    
    if ope == "suma":
        resultado=n1+n2
        print(f'la {ope} de {n1} y {n2} es {resultado}')
    elif ope == "resta":
        resultado=n1-n2
        print(f'la {ope} de {n1} y {n2} es {resultado}')
    elif ope == "multiplicar":
        resultado=n1*n2
        print(f'la {ope} de {n1} y {n2} es {resultado}')
    elif ope == "dividir":
        resultado=n1/n2
        print(f'la {ope} de {n1} y {n2} es {resultado}')
    else:
        resultado=0
        print(f'no se encontro operación solicitada')
        
calculadora(n1=5,n2=10,ope='suma')
calculadora(ope='resta',n1=3,n2=7)
calculadora(ope='multiplicar',n1=3,n2=5)
calculadora(ope='dividir',n1=3,n2=2)