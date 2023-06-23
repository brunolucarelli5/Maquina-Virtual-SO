cadena = hex(int("00001111", 2)).upper()
hexa = cadena[2:len(cadena)]

if len(hexa) == 1:
    hexa = '0' + hexa
print(hexa)