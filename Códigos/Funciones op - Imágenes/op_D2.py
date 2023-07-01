def op_D2(parámetros, memoria):
    dirección_origen = concatenar_hex(parámetros[1],parámetros[2])
    dirección_origen = int(dirección_origen, 16)
    dirección_destino = concatenar_hex(parámetros[3],parámetros[4])
    dirección_destino = int(dirección_destino,16)

    if (dirección_origen <= 65534 and dirección_origen >= 1025) and (dirección_destino <= 65534 and dirección_destino >= 1025):
        memoria[dirección_destino] = memoria[dirección_origen] % memoria[dirección_destino]
        xp = hex(dirección_destino)
        return xp
    else:
        print(" /!\ Error en la ejecución de D0: Dirección inválida /!\ ") 