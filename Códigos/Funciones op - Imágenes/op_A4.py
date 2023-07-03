def op_A4(parámetros, memoria,xp):
    error = "0"
    vector_auxiliar = [""] * 2
    dirección_origen = int(concatenar_hex(parámetros[1], parámetros[2]),16)
    
    if dirección_origen >= 1025 and dirección_origen <= 65534:
        contenido = memoria[dirección_origen]
        dirección_destino = int(xp, 16)

        if dirección_destino >= 100 and dirección_destino <= 1024:
            memoria[dirección_destino] = contenido
            xp = hex(dirección_destino)

            vector_auxiliar[0] = error
            vector_auxiliar[1] = xp

            return vector_auxiliar
        else:
            error = "1"
            print(" /!\ Error en la ejecución de A4: Dirección inválida /!\ ")
            vector_auxiliar[0] = error
            vector_auxiliar[1] = xp

    else:
        error = "1"
        print(" /!\ Error en la ejecución de A4: Dirección inválida /!\ ")
        vector_auxiliar[0] = error
        vector_auxiliar[1] = xp

        return vector_auxiliar