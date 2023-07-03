def op_B1(parámetros,ip):
    error = "0"
    vector_auxiliar = [""] * 2
    dirección_salto = concatenar_hex(parámetros[1], parámetros[2])
    dirección_salto = int(dirección_salto, 16)

    if (dirección_salto <= 1024 and dirección_salto >= 100):
        ip = hex(dirección_salto)
        vector_auxiliar[0] = error
        vector_auxiliar[1] = ip
    else:
        error = "1"
        print(" /!\ Error en la ejecución de B1: Dirección inválida /!\ ")
        vector_auxiliar[0] = error
        vector_auxiliar[1] = ip

        return vector_auxiliar