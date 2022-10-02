class Indice:

    def sum2(self,obj):
        numeros = [10,20,10,40,50,60,70]
        result = False
        for i in numeros:
            p = obj - i 
            if p > 0 and p in numeros:
                result = True
                print(str(numeros.index(i))+" || "+str(numeros.index(p)))
        if not result:
            print("No existe esa combinación")

objetivo = int(input('Introduce un número : '))
ind = Indice()
ind.sum2(objetivo)