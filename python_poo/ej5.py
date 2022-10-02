class Persona():

    def __init__(self,nombre="",edad=0,dni=""):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni
    
    def nombre(self):
        return self.__nombre
    
    def edad(self):
        return self.__edad

    def dni(self):
        return self.__dni
    
    def set_nombre(self,n):
        self.__nombre=n

    def set_dni(self,d):
        self.__dni=d
      
    def set_edad(self,e):
        if edad < 0:
            print("Edad incorrecta")
            self.__edad=0
        else:
            self.__edad=e
     
    def mostrar(self):
        return "Nombre:"+self.__nombre+" - Edad:"+str(self.__edad)+" - DNI:"+self.__dni

    def esMayorDeEdad(self):
        return self.__edad>=18

p1 = Persona()
Nombre = "Luis"
edad = 21
dni = "7869457D"
p1.set_nombre(Nombre)
p1.set_edad(edad)
p1.set_dni(dni)

print(p1.mostrar())
print(p1.esMayorDeEdad())