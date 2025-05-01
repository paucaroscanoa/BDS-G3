class Automovil:
    #creamos el metodo constructi
    def __init__(self,aa,pl,col,mar):
        self.año=aa
        self.placa=pl
        self.color=col
        self.marca=mar
        
    #metodos
    def encender (self):
        print('encender'+ self.marca)
        
    def avanzar (self):
        print('avanzar'+ self.marca)
    
    def acelerar (self):
        print('acelerar'+ self.marca)
    
    def frenar (self):
        print('frenar'+ self.marca)
        
#Creamos un objeto

vw=Automovil(1970,'CH-1234','Amarillo','Volswagen')
vw.encender()    
vw.acelerar()
vw.frenar()

tico=Automovil(1985,'EJ-45678','Rojo','DAEWOO')
tico.encender()
tico.acelerar()
tico.frenar()

   