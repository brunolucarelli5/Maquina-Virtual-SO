def op_A0(parámetros, memoria):
    error = "0"
    dirección = concatenar_hex(parámetros[1],parámetros[2])
    dirección = int(dirección, 16)
    if dirección <= 65534 and dirección >= 1025:
        memoria[dirección] = parámetros[3]
        
        return error
    else:
        error = "1"
        print(" /!\ Error en la ejecución de A0: Dirección inválida /!\ ")
        return error