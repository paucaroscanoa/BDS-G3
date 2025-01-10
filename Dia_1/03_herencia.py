class Persona:
    def __init__(self,dni,nombre,email):
        self.nombre=nombre
        self.dni=dni
        self.email=email
        
    def mostrar(self):
        print("*"*50)
        print(f"DNI : {self.dni}")
        print(f"NOMBRE : {self.nombre}")
        print(f"EMAIL : {self.email}")
        
class Alumno(Persona):
    pass
        

class Profesor(Persona):
    def __init__(self, dni, nombre, email,especialidad):
        super().__init__(dni, nombre, email)
        self.especialidad= especialidad
        
    def mostrar(self):
        print("*"*50)
        print(f"DNI : {self.dni}")
        print(f"NOMBRE : {self.nombre}")
        print(f"EMAIL : {self.email}")
        print(f"ESPECIALIDAD : {self.especialidad}")
     
class Empleado(Persona):
    pass   

alumno1=Alumno(100,'jorge','jorge@gmail.com')
alumno1.mostrar()

profe1=Profesor(200,'Juan','juan@gmail.com','Machine Learning')
profe1.mostrar()

empleado1=Empleado(300,'Pedro','pedro@gmail.com')
empleado1.mostrar()

