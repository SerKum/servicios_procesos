class Cuenta():

    def __init__(self,titular="",cantidad=0):
        self.titular=titular
        self.cantidad=cantidad
    
    def titular(self):
        return self.titular
    
    def cantidad(self):
        return self.cantidad

    def set_titular(self,titular):
        self.titular=titular

    def mostrar(self):
        return "Cuenta\n"+"Titular:"+self.titular+" - Cantidad:"+str(self.cantidad)
    
    def ingresar(self,cantidad):
        if cantidad > 0:
            self.cantidad = self.cantidad + cantidad
    
    def retirar(self,cantidad):
        if cantidad > 0:
            self.cantidad = self.cantidad - cantidad

c1 = Cuenta()
c1.set_titular("Manolo")
c1.ingresar(1000)
print(c1.mostrar())
c1.ingresar(200)
print(c1.mostrar())
c1.retirar(300)
print(c1.mostrar())