def op_A0(parámetros, memoria):
    dirección = concatenar_hex(parámetros[1],parámetros[2])
    dirección = int(dirección, 16)
    if dirección <= 65534 and dirección >= 1025:
        memoria[dirección] = parámetros[3]
        return 0 #Operación exitosa: Devolvemos 0
    else:
        return 1 #Operación fallida: Devolvemos un entero positivo acorde a la documentación  