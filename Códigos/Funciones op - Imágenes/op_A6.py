def op_A6(parámetros, memoria,xp):
    error = "0"
    vector_auxiliar = [""] * 2
    dirección_destino = int(concatenar_hex(parámetros[1], parámetros[2]), 16)
    dirección_destino_siguiente = dirección_destino + 1

    if dirección_destino >=1025 and dirección_destino <= 65533:
        x = xp[2:4]
        p = xp[4:len(xp)]
        memoria[dirección_destino] = x
        memoria[dirección_destino_siguiente] = p
        xp = hex(dirección_destino_siguiente)
        vector_auxiliar[0] = error
        vector_auxiliar[1] = xp

        return vector_auxiliar
    else: 
        error = "1"
        print(" /!\ Error en la ejecución de A6: Dirección inválida /!\ ")
        vector_auxiliar[0] = error
        vector_auxiliar[1] = xp

        return vector_auxiliar