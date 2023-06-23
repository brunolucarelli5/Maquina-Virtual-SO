def cargar(cod_binario, memoria):
    longitud = len(str(cod_binario))
    bandera = False
    instruc = ""
    hexa = ""
    a = 0
    b = 8
    i = 0

    while bandera != True: 
        instruc = str(cod_binario)[a:b]
        hexa = hex(int(instruc, 2))
        
        memoria[i] = hexa
        i += 1

        a = b
        if b == (longitud) and i <= 99:
            bandera = True
        b = b + 8

    return memoria   