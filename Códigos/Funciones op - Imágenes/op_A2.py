def op_A2(parámetros, memoria):
    dirección = concatenar_hex(parámetros[1],parámetros[2])
    dirección = int(dirección, 16)
    if dirección <= 65534 and dirección >= 1025:
        ip = memoria[dirección]
        return 0 #Operación exitosa
    else:
        return 3 #Operación fallida