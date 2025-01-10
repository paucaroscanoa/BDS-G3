class Usuario:
    #para proteger el cambio incluir doble guion en email y password
    __email='ingmariopaucar@gmail.com'
    __password='123456'
    
    def __init__(self):
        pass
    
    def set_password(self,password):
        self.__password=password
    
    def login(self,email,password):
        if(self.__email==email and self.__password==password):
            print(f'Bienvenido {self.__email}')
        else:
            print('datos incorrectos')

print('LOGIN DE USUARIOS')
email=input('Ingrese Email:')
password=input('Ingrese password :')

usuario=Usuario()
#al incluir doble guión proteje que el código sea alterado
usuario.set_password(password)
usuario.login(email,password)


        
    
    
    