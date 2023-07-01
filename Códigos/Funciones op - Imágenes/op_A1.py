def op_A1(parámetros, memoria):
    dirección = concatenar_hex(parámetros[1],parámetros[2])
    dirección = int(dirección, 16)
    if dirección <= 65534 and dirección >= 1025:
        memoria[dirección] = ip
        return 0 #Operación exitosa
    else:
        return 2 #Operación fallida
