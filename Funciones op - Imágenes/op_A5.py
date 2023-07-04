def op_A5(parámetros, memoria,xp):
    error = "0"
    vector_auxiliar = [""] * 2
    dirección_destino = int(concatenar_hex(parámetros[1], parámetros[2]), 16)

    if dirección_destino >= 1025 and dirección_destino <= 65534:
        dirección_origen = int(xp, 16)
        contenido = memoria[dirección_origen]
        memoria[dirección_destino] = contenido
        xp = hex(dirección_destino)
        vector_auxiliar[0] = error
        vector_auxiliar[1] = xp

        return vector_auxiliar
    else: 
        error = "1"
        print(" /!\ Error en la ejecución de A5: Dirección inválida /!\ ")
        vector_auxiliar[0] = error
        vector_auxiliar[1] = xp

        return vector_auxiliar