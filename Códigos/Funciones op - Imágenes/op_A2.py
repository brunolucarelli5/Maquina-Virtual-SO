def op_A2(parámetros, memoria,xp,ip):
    vector_auxiliar = [""] * 2

    dirección = concatenar_hex(parámetros[1],parámetros[2])
    dirección = int(dirección, 16)

    if dirección <= 65533 and dirección >= 1025:

        valor_ip = hex(int(concatenar_hex(memoria[dirección],memoria[dirección+1]),16))
        xp = hex(dirección)

        if int(valor_ip,16) <= 1024 and int(valor_ip,16) >= 100:

            vector_auxiliar[0] = xp
            vector_auxiliar[1] = valor_ip
            
            return vector_auxiliar
    else:
        print(" /!\ Error en la ejecución de A2: Dirección inválida /!\ ")
        vector_auxiliar[0] = xp
        vector_auxiliar[1] = ip
            
        return vector_auxiliar