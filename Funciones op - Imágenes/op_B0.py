def op_B0(parámetros, memoria,ip):
    #El primer elemento del vector es el estado de ejecución, el segundo es el valor de IP
    error = "0"
    vector_auxiliar = [""] * 2

    dirección_salto = concatenar_hex(parámetros[1], parámetros[2])
    dirección_salto = int(dirección_salto, 16)

    dirección_verificación = concatenar_hex(parámetros[3], parámetros[4])
    dirección_verificación = int(dirección_verificación, 16)

    if (dirección_salto <= 1024 and dirección_salto >= 100) and (dirección_verificación <= 65534 and dirección_verificación >= 1025):

        if memoria[dirección_verificación] == hex(0x0):
            ip = hex(dirección_salto)

            vector_auxiliar[0] = error
            vector_auxiliar[1] = ip
            return vector_auxiliar
        
        else:
            vector_auxiliar[0] = error
            vector_auxiliar[1] = ip
            return vector_auxiliar
            
    else:
        error = "1"
        print(" /!\ Error en la ejecución de A6: Dirección inválida /!\ ")
        vector_auxiliar[0] = error
        vector_auxiliar[1] = ip

        return vector_auxiliar