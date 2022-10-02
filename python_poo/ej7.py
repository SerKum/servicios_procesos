from ej6 import Cuenta
class CuentaJoven(Cuenta):

    def __init__(self,titular="",cantidad=0,bonificacion=0,edad=17):
        super().__init__(titular,cantidad)
        self.bonificacion=bonificacion
        self.edad=edad
    
    def bonificacion(self):
        return self.bonificacion
    
    def set_bonificacion(self,bonificacion):
        self.bonificacion=bonificacion

    def mostrar_bonificacion(self):
        return "Cuenta Joven\n"+"Titular:"+self.titular+" - Cantidad:"+str(self.cantidad)+ "- Bonificación:"+str(self.bonificacion)+"%"
   
    def esTitularValido(self):
        return self.edad < 25 and self.esMayorDeEdad()
    
    def esMayorDeEdad(self):
        if self.edad >= 18 :
            return True

    def retirar(self,cantidad):
        if not self.esTitularValido():
            print ("No puedes retirar el dinero. titular no válido")
        elif cantidad > 0:
            super().retirar(cantidad)

c2 = CuentaJoven()
c2.set_titular("Emiliano")
c2.set_bonificacion(45)
print(c2.retirar(400))
print(c2.mostrar_bonificacion())
print(c2.esTitularValido())
c2.retirar(100)