def op_A2(parametro):
    dirección_origen = str(parámetros[0]) + str(parámetros[1])
    dirección_origen = int(dirección_origen,16)
    dirección_destino = str(parámetros[2]) + str(parámetros[2])
    dirección_destino = int(dirección_destino,16)
    if (dirección_origen <= 65534 and dirección_origen >= 1025) and (dirección_destino <= 65534 and dirección_destino >= 1025):
        memoria[dirección_destino] = memoria[dirección_origen]
