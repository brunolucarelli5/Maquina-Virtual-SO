def op_A1(parámetros, memoria):
    dirección = concatenar_hex(parámetros[1],parámetros[2])
    dirección = int(dirección, 16)
    if dirección <= 65534 and dirección >= 1025:
        memoria[dirección] = ip

        xp = hex(dirección)
        return xp
    else:
        print(" /!\ Error en la ejecución de A1: Dirección inválida /!\ ")