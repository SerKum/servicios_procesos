class Parentesis:

    def validar(self,cadena):
        abierto = ["[","{","("]
        cerrado = ["]","}",")"]
        pila = []
        for i in cadena:
            if i in abierto:
                pila.append(i)
            elif i in cerrado:
                pos = cerrado.index(i)
                if((len(pila) > 0) and (abierto[pos] == pila[len(pila) - 1])):
                    pila.pop()
                else:
                    return "Ta' mal"
        if len(pila) == 0:
            return "Ta' bien"
        else:
            return "Ta' mal"



texto = str(input('Introduce una cadena de paréntesis : '))

prueba = Parentesis()
print(str(prueba.validar(texto)))
