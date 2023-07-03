def op_A2(parámetros, memoria,ip):
    dirección = concatenar_hex(parámetros[1],parámetros[2])
    dirección = int(dirección, 16)
    if dirección <= 65533 and dirección >= 1025:

        ip = hex(int(concatenar_hex(memoria[dirección],memoria[dirección+1]),16))
        xp = hex(dirección)

        vector_auxiliar = [""] * 2
        vector_auxiliar[0] = xp
        vector_auxiliar[1] = ip
        
        return vector_auxiliar
    else:
        print(" /!\ Error en la ejecución de A2: Dirección inválida /!\ ")