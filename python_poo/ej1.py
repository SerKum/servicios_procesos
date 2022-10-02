class convertir():
    def ent_a_rom(self,n):
        integer_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        roman = ''
        while n > 0: 
            for i, r in integer_roman: 
                while n >= i: 
                    roman += r 
                    n -= i 
        return roman 
              



num = int(input('Introduce un número : '))
conv = convertir()
print(conv.ent_a_rom(num))