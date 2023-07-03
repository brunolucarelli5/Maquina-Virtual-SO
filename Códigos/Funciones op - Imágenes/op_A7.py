def op_A7(parámetros, memoria):
    dirección_origen = int(concatenar_hex(parámetros[1], parámetros[2]), 16) 
    dirección_origen_siguiente = dirección_origen + 1
        
    if dirección_origen >= 1025 and dirección_origen <= 65533:
        contenido = memoria[dirección_origen] + memoria[dirección_origen_siguiente][2:]
        xp = contenido
        return xp
    else:
            print(" /!\ Error en la ejecución de A7: Dirección inválida /!\ ")