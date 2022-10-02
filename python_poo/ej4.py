class Cadena:
    
    cadena = ''

    def get_string(self):
        self.cadena = str(input('Introduce una frase : '))
    def print_string(self):
        self.cadena.upper()
        print(self.cadena)
    def rev_string(self):
        print(self.cadena[::-1])


texto = Cadena()

texto.get_string()
texto.print_string()
texto.rev_string()