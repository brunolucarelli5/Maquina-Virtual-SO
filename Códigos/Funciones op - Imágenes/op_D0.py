def op_D0(parámetros, memoria, xp):
    dirección_origen = int(concatenar_hex(parámetros[1],parámetros[2]), 16)
    dirección_destino = int(concatenar_hex(parámetros[3],parámetros[4]), 16)

    if (dirección_origen <= 65534 and dirección_origen >= 1025) and (dirección_destino <= 65534 and dirección_destino >= 1025):
        sumando1 = int(memoria[dirección_origen], 16)
        sumando2 = int(memoria[dirección_destino], 16)
        suma = sumando1 + sumando2
        
        #Se toman los bits más significativos en caso de ser necesario
        if suma > 255 or suma < 0:
            suma = hex(suma)
            suma = "0x" + suma[len(suma) - 2 :]
        else:
            suma = hex(suma)
        memoria[dirección_destino] = suma
        xp = hex(dirección_destino)
        
        return xp
    else:
        print(" /!\ Error en la ejecución de D0: Dirección inválida /!\ ")