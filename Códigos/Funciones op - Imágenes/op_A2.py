def op_A2(parámetros, memoria):
    dirección = concatenar_hex(parámetros[1],parámetros[2])
    dirección = int(dirección, 16)
    if dirección <= 65534 and dirección >= 1025:
        ip = memoria[dirección]
        xp = hex(dirección)

        return xp
    else:
        print(" /!\ Error en la ejecución de A2: Dirección inválida /!\ ")